# =============================================================================
# PREPARATION
# =============================================================================

from sklearn.metrics import accuracy_score, recall_score, precision_score, roc_auc_score, f1_score
from sklearn.model_selection import train_test_split # from sklearn.model_selection import KFold
# from dslabs_functions import CLASS_EVAL_METRICS, run_NB, run_KNN, evaluate_approach
from sklearn.impute import SimpleImputer, KNNImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import KBinsDiscretizer
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from imblearn.over_sampling import SMOTE
from sklearn.decomposition import PCA # Feature Engeneering
#from dslabs_functions import select_low_variance_variables, study_variance_for_feature_selection, apply_feature_selection
#from dslabs_functions import select_redundant_variables, study_redundancy_for_feature_selection




# 1. Variable Encoding
def encode_binary_and_symbolic_variables(data: DataFrame, vars: list[str], encoding: dict[str, dict[str, int]] = {}):
    # Ordinal Encoding # Cuidado que esta função vai fazer encoding das variáveis cíclicas que estão classificadas como simbólicas. # O melhor é alterar a função para receber quais as variáveis que se pretendem fazer enconding
    #df: DataFrame = data.copy(deep=True) #encoding: dict[str, dict[str, int]] = {}
    if encoding == {}: 
        for var in vars:
            if var in (get_variable_types(data)['binary']) or var in (get_variable_types(data)['symbolic']):
                unique_values = list(data[var].dropna().unique()); unique_values.sort()
                encoding[var] = {x: int(i) for i,x in enumerate(unique_values)}
                #print(var, encoding[var])
    if encoding != {}: df: DataFrame = data.replace(encoding, inplace=False) #df.head() #print(get_variable_types(df))
    return df
def encode_cyclic_variables(data: DataFrame, vars: list[str]) -> None:
    # Cyclic variables Encoding
    df: DataFrame = data.copy(deep=True)
    encoding: dict = {}
    for v in vars:
        vals = list(df[v].dropna().unique()) # Necessário verificar se a ordem entre os valores está correta: Exemplo: ['autumn', 'winter', 'spring', 'summer'] 
        var_encoding: dict[str, float] = {val: i*(2*pi/len(vals)) if i*(2*pi/len(vals)) <= pi else i*(2*pi/len(vals)) - 2*pi for i,val in enumerate(vals)} #k = len(vals); passo = (2*pi/k) #season_val: dict[str, float] = {"spring": 0, "summer": pi / 2, "autumn": pi, "winter": -pi / 2}
        encoding[v] = var_encoding
        df.replace(encoding, inplace=True)
    
    for v in vars:
        x_max: float | int = max(df[v])
        df[v + "_sin"] = df[v].apply(lambda x: round(sin(2 * pi * x / x_max), 3))
        df[v + "_cos"] = df[v].apply(lambda x: round(cos(2 * pi * x / x_max), 3))
    return df
def dummify_variables(data: DataFrame, vars: list[str]) -> DataFrame:
    # Dummification or One-hot Encoding
    enc = OneHotEncoder(handle_unknown="ignore", sparse_output=False, dtype="bool", drop="if_binary") #from sklearn.preprocessing import OneHotEncoder
    trans: ndarray = enc.fit_transform(data[vars])
    new_vars: ndarray = enc.get_feature_names_out(vars)
    dummy = DataFrame(trans, columns=new_vars, index=data.index)
    other_vars: list[str] = [c for c in data.columns if c not in vars] # [c for c in data.columns if not c in vars]
    df: DataFrame = concat([data[other_vars], dummy], axis=1)
    
    #dummy_encoded = encode_binary_and_symbolic_variables(dummy, list(new_vars))
    #df: DataFrame = concat([data[other_vars], dummy_encoded], axis=1)
    return df
#df: DataFrame = encode_binary_and_symbolic_variables(data_cancer, list(data_cancer.columns))
#df: DataFrame = encode_binary_and_symbolic_variables(data_algae, [var for var in data_algae.columns if var != 'season'])
#df: DataFrame = encode_cyclic_variables(data, ["season"]) #print(data.head())
#df: DataFrame = dummify_variables(data_algae, ["river_depth", "fluid_velocity", "season"]) #df.head()

# 2. Missing Values Imputation
def mvi_by_dropping(data: DataFrame, type1: str = "records", type2: str = "any", min_pct_per_var: float = 0.1, min_pct_per_rec: float = 0.0) -> DataFrame:
    # Dropping Missing Values
    if type1 == "records":
        if type2 == "any": # Drop records that have any missing value (some variables)
            df: DataFrame = data.dropna(how="any", inplace=False)# Another interesting parameter is how, which allows for determining which records are deleted: any establishes that a record is deleted if any of its variable values is missing, or it requires them all to be missing (all).
        elif type2 == "all": # Drop records that have all missing values (all variables)
            df: DataFrame = data.dropna(how="all", inplace=False) # If we used the all option, however, we wouldn't be able to delete any record, since we just have MVs in two variables.
    elif type1 == "variables":
        if type2 == "any": # Drop variables that have any missing value
            df: DataFrame = data.dropna(axis=1, how="any", inplace=False) # In this situation, it would be preferable to eliminate the smoking_status variable, which just require the use of another parameter - the axis, setting it to 1. However, just by doing it, the variable bmi would also be discarded, which might be harmfull to the information discovery.
        elif type2 == "all": # Drop variables that have all missing values
            df: DataFrame = data.dropna(axis=1, how="all", inplace=False)
    elif type1 == "both":
        # Another option might be to only drop variables or records that show valid values above a given threshold - through the use of the thresh parameter.
        df: DataFrame = data.dropna(axis=1, thresh=data.shape[0] * min_pct_per_var, inplace=False) # Deleting variables
        df.dropna(axis=0, thresh=data.shape[1] * min_pct_per_rec, inplace=True) # Deleting records
    return df
def mvi_by_filling(data: DataFrame, strategy: str = "frequent") -> DataFrame:
    # Filling missing values
    # As several other classes in sklearn, the imputer is declared choosing its specific strategy (strategy parameter), then it is fitted to the data where it is to be applied (fit method), and then applied (transformmethod). 
    # Among the available strategies to fill any missing value with a new value, we find: # constant: the constant value chosen depends on the type of variable (usually: NaN, -1 or 0 for numeric, 'NA' for symbolic and False for boolean); # mean, median and most_frequent: the first two only applicable for numeric variables, and the last one mostly interesting for symbolic variables;
    # The function mvi_by_filling defined next, can be used to fill any missing value, using a single strategy to all kinds of variables in a dataset.
    variables: dict = get_variable_types(data); numeric, symbolic, binary = variables["numeric"], variables["symbolic"], variables["binary"]
    
    stg_num, v_num = "mean", -1 # "median", "most_frequent"
    stg_sym, v_sym = "most_frequent", "NA"
    stg_bool, v_bool = "most_frequent", False
    
    if strategy != "KNN": # Be aware that filling missing values with already existing values, such as 0, -1 or False changes the data distribution. For this reason, it is usually to apply the frequent strategy (mean and mode) instead.
        lst_dfs: list = []
        
        if strategy == "constant": stg_num, stg_sym, stg_bool = "constant", "constant", "constant"
            
        if numeric != []:
            imp = SimpleImputer(strategy=stg_num, fill_value=v_num, copy=True)
            tmp_nr = DataFrame(imp.fit_transform(data[numeric]), columns=numeric)
            lst_dfs.append(tmp_nr)
        
        if symbolic != []:
            imp = SimpleImputer(strategy=stg_sym, fill_value=v_sym, copy=True)
            tmp_sb = DataFrame(imp.fit_transform(data[symbolic]), columns=symbolic)
            lst_dfs.append(tmp_sb)
        
        if binary != []:
            imp = SimpleImputer(strategy=stg_bool, fill_value=v_bool, copy=True)
            tmp_bool = DataFrame(imp.fit_transform(data[binary]), columns=binary)
            lst_dfs.append(tmp_bool)
        
        df: DataFrame = concat(lst_dfs, axis=1)
        print(f"MVI {strategy} strategy", df.describe())
    else: # Note however, that like for other applications, KNNImputer doesn't work over non-numeric data, and so, variable encoding had to be applied beforehand.
        imp = KNNImputer(n_neighbors=5)
        imp.fit(data)
        ar: ndarray = imp.transform(data)
        df: DataFrame = DataFrame(ar, columns=data.columns, index=data.index)
        print(f"MVI {strategy} strategy", df.describe())
    # Don't forget to save the resulting data to a datafile, to be used for training models and discovering other kinds of information.
    return df
#df: DataFrame = mvi_by_dropping(data_algae, type1="both", min_pct_per_var=0.7, min_pct_per_rec=0.9)
#df: DataFrame = mvi_by_dropping(data_algae, type1="records", type2="any", min_pct_per_var=0.7, min_pct_per_rec=0.9)
#df: DataFrame = mvi_by_filling(data_cancer, strategy="frequent") #df: DataFrame = mvi_by_filling(data_cancer, strategy="constant")
#numeric: list[str] = get_variable_types(data_algae)["numeric"]; data_algae[["Chlorophyll", "Chloride"]].describe() # Now, look at the five number summary for the dataset after applying a frequent and a KNN MVI strategy, respectively. Pay attention to the Chlorophyll and Chloride variables. 
#df: DataFrame = mvi_by_filling(data_algae[numeric], strategy="frequent") #df[["Chlorophyll", "Chloride"]].describe()
#df: DataFrame = mvi_by_filling(data_algae[numeric], strategy="KNN") #df[["Chlorophyll", "Chloride"]].describe()



# 4. Outliers treatment
def outliers(data: DataFrame, nrstdev: int | float = 2):
    # Por aqui a função "determine_outlier_thresholds_for_var"
    #NR_STDEV: int = 2.5 #2
    numeric: list[str] = get_variable_types(data)["numeric"]
    
    # Dropping Outliers
    def dropping_outliers(data, nrstdev, numeric):
        # The easiest way to deal with this situation is to drop the records with outliers. Note that we make a copy of the original data (copy method from the DataFrame class), in order to not impact on the following approaches.
        df: DataFrame = data.copy(deep=True); summary5: DataFrame = data[numeric].describe(include="all")
        for var in numeric:
            top_threshold, bottom_threshold = determine_outlier_thresholds_for_var(summary5[var], std_based=True, threshold=nrstdev)
            outliers: Series = df[(df[var] > top_threshold) | (df[var] < bottom_threshold)]
            df.drop(outliers.index, axis=0, inplace=True)
        df.name = "Dropping Outliers"
        #df.to_csv(f"data/{file_tag}_drop_outliers.csv", index=True)
        #df.shape # print(f"Data after dropping outliers: {df.shape}")
        return df
    
    # Replacing outliers with fixed value
    def replacing_outliers_with_fixed_value(data, nrstdev, numeric):
        # Instead of dropping all the records with outliers, it is also possible to replace the outliers with a fixed value, for example its median value.
        df: DataFrame = data.copy(deep=True); summary5: DataFrame = data[numeric].describe(include="all")
        for var in numeric:
            top, bottom = determine_outlier_thresholds_for_var(summary5[var], std_based=True, threshold=nrstdev)
            median: float = df[var].median()
            df[var] = df[var].apply(lambda x: median if x > top or x < bottom else x)
        df.name = "Replacing outliers with fixed value"
        #df.to_csv(f"data/{file_tag}_replacing_outliers.csv", index=True)
        #df.shape # print("Data after replacing outliers:", df.shape) #df.describe() #print(df.describe())
        return df
    
    # Truncating outliers
    def truncating_outliers(data, nrstdev, numeric):
        # Another possibility is to truncate the outliers to the minimum/maximum accepted as regular objects, which can be done as follows, using the previous determine_outlier_thresholds function.
        df: DataFrame = data.copy(deep=True); summary5: DataFrame = data[numeric].describe(include="all")
        for var in numeric:
            top, bottom = determine_outlier_thresholds_for_var(summary5[var], std_based=True, threshold=nrstdev)
            df[var] = df[var].apply(lambda x: top if x > top else bottom if x < bottom else x)
        df.name = "Truncating outliers"
        #df.to_csv(f"data/{file_tag}_truncate_outliers.csv", index=True)
        #df.shape # print("Data after replacing outliers:", df.shape) #df.describe() #print(df.describe())
        return df
    
    # NOTA: Em vez de trocar os outliers por números, também dá para os substituir por missing values -> Escrever esse código
    # É a mesma função que "replacing_outliers_with_fixed_value" mas em vez da mediana para trocar o valor, tem de se colocar "nan"
    
    if numeric != []:
        dfd: DataFrame = dropping_outliers(data, nrstdev, numeric)
        dfr: DataFrame = replacing_outliers_with_fixed_value(data, nrstdev, numeric)
        dft: DataFrame = truncating_outliers(data, nrstdev, numeric)
        plot_multi_boxplots([dfd, dfr, dft])
        
    else: print("There are no numeric variables")
    
    return dfd, dfr, dft
dfd, dfr, dft = outliers(data_algae, nrstdev=2) #data_algae: DataFrame = read_csv("data/algae.csv", index_col="date", na_values="", parse_dates=True, dayfirst=True)



# 3. Discretization
def discretization(data: DataFrame, n_bins: int = 5):
    # Discretization only applies to numerical variables, and may be accomplished using both an equal-with and equal-frequency strategies. These strategies are implemented in sklearn.preprocessing package through the KBinsDiscretizer class. For that we just need to choose strategy="uniform" and strategy="quantile", respectively.
    # The number of intervals to consider is specified by the n_bins parameter.
    # N_BINS = 5
    
    vars: list[str] = list(data.columns)
    
    variable_types: dict[str, list] = get_variable_types(data)
    
    numeric: list[str] = variable_types["numeric"]
    symbolic: list[str] = variable_types["symbolic"]
    boolean: list[str] = variable_types["binary"]
    
    df_nr: DataFrame = data[numeric]
    df_sb: DataFrame = data[symbolic]
    df_bool = data[boolean]
    
    # Equal-width discretization
    def equal_width_discretization(data, n_bins):
        # Note the similarity of these histograms to the ones plotted before (Data Profiling - Distribution).
        discretization: KBinsDiscretizer = KBinsDiscretizer(n_bins=n_bins, encode="ordinal", strategy="uniform") #from sklearn.preprocessing import KBinsDiscretizer
        discretization.fit(df_nr)
        eq_width = DataFrame(discretization.transform(df_nr), index=data.index)
        
        df = DataFrame(df_sb, index=data.index)
        df: DataFrame = concat([df, df_bool, eq_width], axis=1)
        df.columns = symbolic + boolean + numeric
        df = df[vars]
        
        plot_histograms(df) #df.hist(bins=N_BINS)
        #savefig(f"images/{file_tag}_histogram_eq_width.png") 
        #df.to_csv(f"data/{file_tag}_eq_width_discretization.csv", index=True)
        return df
    
    # Equal-frequency discretization
    def equal_frequency_discretization(data, n_bins):
        # Note the approximate uniform probability distribution for all the variables.
        discretization: KBinsDiscretizer = KBinsDiscretizer(n_bins=n_bins, encode="ordinal", strategy="quantile")
        discretization.fit(df_nr)
        eq_width = DataFrame(discretization.transform(df_nr), index=data.index)
        
        df = DataFrame(df_sb, index=data.index)
        df = concat([df, df_bool, eq_width], axis=1)
        df.columns = symbolic + boolean + numeric
        df = df[vars]
        
        plot_histograms(df) #df.hist(bins=N_BINS)
        #savefig(f"images/{file_tag}_histogram_eq_frequency.png")
        #df.to_csv(f"data/{file_tag}_eq_frequency_discretization.csv", index=True)
        return df
        
    df_ew: DataFrame = equal_width_discretization(data, n_bins)
    df_ef: DataFrame = equal_frequency_discretization(data, n_bins)
        
    return df_ew, df_ef
df_ew, df_ef = discretization(data_algae, n_bins=5) #data_algae: DataFrame = read_csv("data/algae_mv_most_frequent.csv", index_col="date", na_values="", parse_dates=True)



# 5. Scaling
def scaling(data: DataFrame, target: str = "", show_plot: bool = True):
    # Scaling transformations are useful to reduce all numeric variables to a same range, in order to garantee that variables with larger scales do not assume more importance.# These transformations are particular important when distance-based algorithms are to be used. They can be accomplished by the scalers available in the sklearn.preprocessing package.# Note the use of the parameter copy as True on all scalers, in order to keep the original data unchanged. Additionaly, do not forget that they only work over numeric data.
    # Scaling # As for multivariate data, scaling may be of extreme importance, and it can be achieved in the same way as before, but apllying the transformation to all variables, the target included.
    
    data = data.copy(deep=True); data.name = "Original"
    vars: list[str] = [var for var in data.columns.to_list()] #if var != target]
    
    include_target: bool = target == ""
    target_data: Series | None = data.pop(target) if not(include_target) else None
    
    def standard_scaling(data, vars, target, target_data, include_target):
        # The StandardScaler implements the z-score transformation, transforming each value into a measure of how far it is to the variable mean value. Note that it produces both positive and negative values.
        transf: StandardScaler = StandardScaler(with_mean=True, with_std=True, copy=True).fit(data)
        df_zscore = DataFrame(transf.transform(data), index=data.index)
        if not(include_target): df_zscore[target] = target_data
        df_zscore.columns = vars
        df_zscore.name = "After Z-score Scaling"
        #df_zscore.to_csv(f"data/{file_tag}_scaled_zscore.csv", index="id")
        return df_zscore
    
    def min_max_scaling(data, vars, target, target_data, include_target):
        # The MinMaxScaler maps variables values from their original range to a new fixed one - the same for all variables.# The most usual range is [0, 1], but it can be anything else. Indeed, this range may introduce some additional issues, since the different values become very close. This may be a problem, when the numeric precision needed is too much.
        transf: MinMaxScaler = MinMaxScaler(feature_range=(0, 1), copy=True).fit(data)
        df_minmax = DataFrame(transf.transform(data), index=data.index)
        if not(include_target): df_minmax[target] = target_data
        df_minmax.columns = vars
        df_minmax.name = "After MinMax Scaling"
        #df_minmax.to_csv(f"data/{file_tag}_scaled_minmax.csv", index="id")
        return df_minmax
    
    df_zscore: DataFrame = standard_scaling(data, vars, target, target_data, include_target)
    df_minmax: DataFrame = min_max_scaling(data, vars, target, target_data, include_target)
    
    if show_plot: plot_multi_boxplots([data, df_zscore, df_minmax])
    
    return df_zscore, df_minmax
df_zscore, df_minmax = scaling(data_cancer, target="stroke") #data_cancer: DataFrame = read_csv("data/stroke_mvi_encoded.csv", index_col="id", na_values="")




# 6. Balancing
def balancing(train: DataFrame, target: str):
    # 6. Balancing # When classification is the aim of our analysis, one of the problems to address is data balancing. In this context, we consider a variable to be of interest - the one to learn to distinguish and to predict. Usually it is called the class or target variable.# As seen in the data distribution lab, the balancing encompasses the difference on the frequency of each class. And this situation usually impairs the learning process.# As we can see, the difference between the frequency for Yes and No is huge, and almost all learning techniques will tend to ignore the minority class.# Before proceeding, lets split the dataset into two subdatasets: one for each class. Then we can sample the required one and join to the other one, as we did on the other preparation techniques. In the end, we can write the dataset into a new datafile to explore later.# We can follow different strategies, the choice between them depends on the size of the dataset, i.e., the number of records to use as train:
    
    original: DataFrame = train.copy(deep=True)
    original_target_count: Series = Series(original[target].value_counts().sort_index(), name="Original")
    
    positive_class, negative_class = original_target_count.idxmin(), original_target_count.idxmax() 
    #print_class_info(positive_class, original_target_count[positive_class], negative_class, original_target_count[negative_class], title="ORIGINAL") #plot_bar_chart(target_count.index, target_count, title="Class balance") #savefig(f"images/{file_tag}_bar_chart_class_balance.png")
    
    df_positives: Series = original[original[target] == positive_class]
    df_negatives: Series = original[original[target] == negative_class]
    
    
    def under_samplling(df_positives, df_negatives, target):
        # 1. Undersampling # With a huge dataset, and consequently a considerable number of positve records, we can use an undersampling strategy, keeping the positive records and sampling the negative ones to balance the final distribution
        df_neg_sample: DataFrame = DataFrame(df_negatives.sample(len(df_positives)))
        df_under: DataFrame = concat([df_positives, df_neg_sample], axis=0) #df_under.to_csv(f"data/{file}_under.csv", index=False)
        
        under_target_count: Series = Series(df_under[target].value_counts().sort_index(), name="Under") #print_class_info(positive_class, len(df_positives), negative_class, len(df_neg_sample), title="UNDER BALANCING")
        return df_under, under_target_count
    
    def over_sampling(df_positives, df_negatives, target):
        # 2. Oversampling # In the presence of a small number of positive records, we need to apply oversampling, in order to create a larger set to support the training step. # And we get oversampling by replication in a similar way. 
        df_pos_sample: DataFrame = DataFrame(df_positives.sample(len(df_negatives), replace=True)) # Note on the replace parameter in the sample method, which means that we are taking a sample with replacement, meaning that we pick the same record more than once.
        df_over: DataFrame = concat([df_pos_sample, df_negatives], axis=0) #df_over.to_csv(f"data/{file}_over.csv", index=False)
        
        over_target_count: Series = Series(df_over[target].value_counts().sort_index(), name="Over") #print_class_info(positive_class, len(df_pos_sample), negative_class, len(df_negatives), title="OVER BALANCING")
        return df_over, over_target_count
    
    def hybrid_sampling(df_positives, df_negatives, target, pos_class_pct_of_negative_class: float = 0.5):
        # 3. Hybrid strategy # Naturally, we may opt to just take a sample of the negative subset and join it to a replication of the entire positives subset, in order to have the same number of records for both. This is usually known as an hybrid approach. Or even to get a non-perfect balanced dataset, to avoid giving too much importance to the positive class.
        target_size = ceil(pos_class_pct_of_negative_class * len(df_negatives)) if pos_class_pct_of_negative_class >= len(df_positives) / len(df_negatives) else ceil((len(df_positives) / len(df_negatives)) * len(df_negatives)) # Necessário colocar um if nisto para não exceder 100% nem ser inferior a à percentagem que já representa inicialmente nos negativos
        df_neg_sample = df_negatives.sample(target_size) # Undersampling Negatives (Majority class)
        df_pos_sample = df_positives.sample(target_size, replace=True) # Oversampling Positives (Minority class)
        df_hybrid = concat([df_pos_sample, df_neg_sample], axis=0) #df_hybrid.to_csv(f"data/{file}_under.csv", index=False)
        
        hybrid_target_count: Series = Series(df_hybrid[target].value_counts().sort_index(), name="Hybrid") #print_class_info(positive_class, len(df_pos_sample), negative_class, len(df_neg_sample), title="HYBRID BALANCING")
        return df_hybrid, hybrid_target_count
    
    def SMOTE_balancing(original: DataFrame, target, random_state: int | None = None):
        # 4. SMOTE # Among the different oversampling strategies there is SMOTE, one of the most interesting ones. In this case, the oversample is created from the minority class, by artificially creating new records in the neighborhood of the positive records.# It is usual to adopt a hybrid approach, by choosing a number of records between the number of positives and negatives, say N. This however implies taking a sample from the negatives with N records, and generating the new positives ones reaching the same number of records.# Note that this technique only deals with numeric variables, so we need to ensure that all symbolic variables were previously encoded.
        smote: SMOTE = SMOTE(sampling_strategy="minority", random_state=random_state) #from imblearn.over_sampling import SMOTE
        y = original.pop(target).values
        X: ndarray = original.values
        smote_X, smote_y = smote.fit_resample(X, y)
        df_smote: DataFrame = concat([DataFrame(smote_X), DataFrame(smote_y)], axis=1)
        df_smote.columns = list(original.columns) + [target] # print(df_smote.shape)
        #df_smote.to_csv(f"data/{file}_smote.csv", index=False)
        
        smote_target_count: Series = Series(Series(smote_y).value_counts().sort_index(), name="SMOTE") #print_class_info(positive_class, smote_target_count[positive_class], negative_class, smote_target_count[negative_class], title="SMOTE BALANCING")
        # See, that for SMOTE method we have to split the original data into two: one with just one variable - the class variable, call it y, and another with all the other variables, call it X (look at the Classification lab for more details about this).# Then the SMOTE technique generates the positive records, don't needing to join the positive and negatives ones. Indeed, what we have to do is just rejoin the data (smote_X) with the corresponding class (smote_y), already updated.# Be carefull with the index parameter: since we are preparing the data for training, we donot need the index, hence we set it to False. Note that when we apply SMOTE, the index of the original data is not kept unchanged, and if required we need to recreate it.
        return df_smote, smote_target_count
    
    def print_class_info(positive_class: int | str, n_positives: int, negative_class: int | str, n_negatives: int, title: str):
        print(f"\n=== {title} ===")
        print("Minority class (Positive class): Value/Label : ", positive_class, ": Count: ", n_positives)
        print("Majority class (Negative class): Value/Label : ", negative_class, ": Count: ", n_negatives)
        print("Proportion: ", round(n_positives / n_negatives, 2)," : 1")
    
    df_under, under_target_count = under_samplling(df_positives, df_negatives, target)
    df_over, over_target_count = over_sampling(df_positives, df_negatives, target)
    df_hybrid, hybrid_target_count = hybrid_sampling(df_positives, df_negatives, target, pos_class_pct_of_negative_class = 0.5)
    df_smote, smote_target_count = SMOTE_balancing(original, target, random_state = None) # random_state = 42
    
    nomes = ["Original", "Under", "Over", "Hybrid", "SMOTE"]
    valores = [original_target_count, under_target_count, over_target_count, hybrid_target_count, smote_target_count]
    values: dict[str, list | dict] = {'0': {nomes[i]: valores[i][0] for i,n in enumerate(nomes)} , '1': {nomes[i]: valores[i][1] for i,n in enumerate(nomes)}} #{"Original": [target_count[positive_class], target_count[negative_class]]}
    
    plot_multi_bar_chart(nomes, values, title="Target class distribuition per balancing strategy", xlabel="Strategy", ylabel="N.º of records")
    
    # Prints aqui para ficar mais limpo
    for i, nome in enumerate(valores):
        print_class_info(positive_class, nome[positive_class], negative_class, nome[negative_class], title=nomes[i]) #plot_bar_chart(target_count.index, target_count, title="Class balance") #savefig(f"images/{file_tag}_bar_chart_class_balance.png")
    
    return df_under, df_over, df_hybrid, df_smote
df_under, df_over, df_hybrid, df_smote = balancing(train, target="stroke") #train: DataFrame = read_csv(f"data/stroke_train.csv", sep=",", decimal=".") #target = "stroke"




# 7. Feature Engineering (Faz mais sentido que seja antes do balancing)

# Feature Selection
def feature_selection(train: DataFrame, test: DataFrame, max_threshold: float | int = 1, min_threshold: float = 0.90, file_tag: str = "", target: str = "class"):
    def apply_feature_selection(train: DataFrame, test: DataFrame, vars2drop: list) -> tuple[DataFrame, DataFrame]: #, filename: str = "", tag: str = ""
        # From this verification, we can now save both datasets resulting from dropping those variables. First we identify the variables to drop for the selected threshold - select_low_variance_variables, just like we do through the previous function and then we drop those variables from both the train and test datafiles, saving them permantely
        train_copy: DataFrame = train.drop(vars2drop, axis=1, inplace=False) #train_copy.to_csv(f"{filename}_train_{tag}.csv", index=True)
        test_copy: DataFrame = test.drop(vars2drop, axis=1, inplace=False) #test_copy.to_csv(f"{filename}_test_{tag}.csv", index=True)
        return train_copy, test_copy
    
    # Dropping Low Variance Variables
    def select_low_variance_variables(data: DataFrame, max_threshold: float, target: str = "class") -> list:
        # A variable is said to be relevant when it contributes to discriminate among the classes. Since a variable may be relevant for one classification task but irrelevant for another one, we can look at it as a supervised task.
        # However, there are situations when this doesn't happen, and the variables are just irrelevant by nature. This happens for variables with very low variance (when the variable presents almost always the same value) or with the highest possible variance (when the variable is an identifier, presenting a different value for each record). Note however, that having a different value for each record, doesn't imply it is an identifier, and so, for this last situation it is only safe to drop the variable if there is enough domain knowledge to recognize it as an identifier. Remember we can't discard the target variable!
        # In order to discard low variance variables, we need first to identify them, which can be done as in the select_low_variance_variables function, that makes use of the describe method from the DataFrame data object.
        summary5: DataFrame = data.describe()
        vars2drop: Index[str] = summary5.columns[summary5.loc["std"] * summary5.loc["std"] < max_threshold]
        vars2drop = vars2drop.drop(target) if target in vars2drop else vars2drop
        return list(vars2drop.values)
    def study_low_variance_variables(data: DataFrame, max_threshold: float | int, target: str = "class"):
        xvalues = {round(i,1): i for i in arange(0, max_threshold + 0.1, 0.1)}
        yvalues = {i: len(select_low_variance_variables(data, i, target=target)) for i in xvalues}
        #print({round(i,1): len(select_low_variance_variables(train, i, target=target)) for i in xvalues})
        plot_line_chart(xvalues, yvalues, title="N.º of low variance variables to drop per threshold", xlabel="max_threshold", ylabel="N.º of variables to drop" )
    def study_variance_for_feature_selection(train: DataFrame, test: DataFrame, target: str = "class", max_threshold: float | int = 1, lag: float = 0.05, file_tag: str = "") -> dict:
        # But more than magically choose that threshold, we shall study the impact of different ones in the model performance, so use the study_variance_for_feature_selection function below. It receives both the train and test datasets, to support the training of the classifier and to testing it, respectively, the target variable, the max_threshold value to consider as the maximum low variance threshold, the lag to pace the change on the threshold value to change, the metric to optimize and a file_tag to facilitate managing the charts.
        options: list[float] = [round(i * lag, 3) for i in range(1, ceil(max_threshold / lag + lag))]
        results: dict[str, list] = {"NB": {}, "KNN": {}}
        summary5: DataFrame = train.describe()
        
        rows, cols = len(CLASS_EVAL_METRICS), 1
        fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 3, rows * HEIGHT), squeeze=False) #dpi=300
        #fig.suptitle("Nr of standard and non-standard outliers per variable")
        i, j = 0, 0
        for i, metric in enumerate(CLASS_EVAL_METRICS):
            for thresh in options:
                vars2drop: list[str] = select_low_variance_variables(train, max_threshold=thresh, target=target)
                train_copy, test_copy = apply_feature_selection(train, test, vars2drop) #train_copy: DataFrame = train.drop(vars2drop, axis=1, inplace=False) #test_copy: DataFrame = test.drop(vars2drop, axis=1, inplace=False)
                eval: dict[str, list] | None = evaluate_approach(train_copy, test_copy, target=target, metric=metric)
                if eval is not None:
                    results["NB"][thresh] = eval[metric]["NB"]
                    results["KNN"][thresh] = eval[metric]["KNN"]
            plot_multi_line_chart(options, results, ax=axs[i,j], title=f"{file_tag} variance study ({metric})", xlabel="variance threshold", ylabel=metric, percentage=True, show_plot = False) #savefig(f"images/{file_tag}_fs_low_var_{metric}_study.png")
        show()    
    study_low_variance_variables(train, max_threshold=2, target=target)
    study_variance_for_feature_selection(train, test, target=target, max_threshold=max_threshold, lag=0.1) #), file_tag=file_tag)
    # As we can see, the difference on performance is not strong, but it is slightly better for NB when variables with a variance bellow 1.3 were removed. Note in this case naive Bayes doesn't show any change due to the feature selection, but it can happen.
    
    # Dropping Redundant Variables
    def select_redundant_variables(data: DataFrame, min_threshold: float = 0.90, target: str = "class") -> list:
        # A second possibility is to discard redundant variables. Two variables are said to be redundant if they express the same information. So, from the modeling perspective they both has the same impact over the result. One of the ways to avoid redundancy is to find the set of pairs of correlated variables, and drop one of each pair.
        data = data.copy(deep=True)
        df: DataFrame = data.drop(target, axis=1, inplace=False)
        corr_matrix: DataFrame = abs(df.corr())
        variables: Index[str] = corr_matrix.columns
        vars2drop: list = []
        for v1 in variables:
            vars_corr: Series = (corr_matrix[v1]).loc[corr_matrix[v1] >= min_threshold]
            vars_corr.drop(v1, inplace=True)
            if len(vars_corr) > 1:
                lst_corr = list(vars_corr.index)
                for v2 in lst_corr:
                    if v2 not in vars2drop:
                        vars2drop.append(v2)
        return vars2drop
    def study_redundant_variables(data: DataFrame, min_threshold: float = 0.90, target: str = "class"):
        data = data.copy(deep=True)
        xvalues = {round(i,1): i for i in arange(0, min_threshold + 0.1, 0.1)}
        yvalues = {i: len(select_redundant_variables(data, min_threshold=i, target=target)) for i in xvalues}
        #print( (round(i,1), len(select_redundant_variables(train, target=target, min_threshold=i)), select_redundant_variables(train, target=target, min_threshold=i)) for i in arange(0.1, 0.9 + 0.1, 0.1))
        plot_line_chart(xvalues, yvalues, title="N.º of redundant variables per threshold", xlabel="min_threshold", ylabel="N.º of variables to drop")
    def study_redundancy_for_feature_selection(train: DataFrame, test: DataFrame, target: str = "class", min_threshold: float = 0.90, lag: float = 0.05, file_tag: str = "") -> dict:
        # After being able to select the redundant variables to drop, it is then possible to study the impact of their removal from the training dataset, as done in the study_redundancy_for_feature_selection function.
        train = train.copy(deep=True)
        test = test.copy(deep=True)
        
        options: list[float] = [round(min_threshold + i * lag, 3) for i in range(ceil((1 - min_threshold) / lag) + 1)]
        
        df: DataFrame = train.drop(target, axis=1, inplace=False)
        corr_matrix: DataFrame = abs(df.corr())
        variables: Index[str] = corr_matrix.columns
        results: dict[str, list] = {"NB": {}, "KNN": {}}
        
        rows, cols = len(CLASS_EVAL_METRICS), 1
        fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 3, rows * HEIGHT), squeeze=False) #dpi=300
        #fig.suptitle("Nr of standard and non-standard outliers per variable")
        i, j = 0, 0
        for i, metric in enumerate(CLASS_EVAL_METRICS):
        
            for thresh in options:
                
                #vars2drop: list = select_redundant_variables(train, min_threshold=min_threshold, target=target)
                vars2drop: list = []
                for v1 in variables:
                    vars_corr: Series = (corr_matrix[v1]).loc[corr_matrix[v1] >= thresh]
                    vars_corr.drop(v1, inplace=True)
                    if len(vars_corr) > 1:
                        lst_corr = list(vars_corr.index)
                        for v2 in lst_corr:
                            if v2 not in vars2drop:
                                vars2drop.append(v2)
                
                train_copy, test_copy = apply_feature_selection(train, test, vars2drop)
                #train_copy: DataFrame = train.drop(vars2drop, axis=1, inplace=False)
                #test_copy: DataFrame = test.drop(vars2drop, axis=1, inplace=False)
                
                eval: dict | None = evaluate_approach(train_copy, test_copy, target=target, metric=metric)
                if eval is not None:
                    results["NB"][thresh] = eval[metric]["NB"]
                    results["KNN"][thresh] = eval[metric]["KNN"]
            
            plot_multi_line_chart(options, results, ax=axs[i,j], title=f"{file_tag} redundancy study ({metric})", xlabel="correlation threshold", ylabel=metric, percentage=True, show_plot = False) #savefig(f"images/{file_tag}_fs_redundancy_{metric}_study.png")
        show()
    study_redundant_variables(train, min_threshold=1, target=target)
    study_redundancy_for_feature_selection(train, test, target=target, min_threshold=min_threshold, lag=0.05, file_tag=file_tag)
    # From these results, it is clear that removing low correlated variables has a negative impact on the selected modeling techniques, much stronger for Naive Bayes than for KNN, in this case study.
    # The best results for naive Bayes are when we discard variables with a correlation higher than 0.5, but for KNN it is preferable to drop for correlations above 0.4. Since the improvement for naive Bayes is much higher, we choose to do it choosing a threshold of 0.5.
    # We could then run the apply_feature_selection function, as before, but now after applying the select_redundant_variables with the min_threshold = 0.5.
    
    
    vars2drop_lv: list[str] = select_low_variance_variables(train, max_threshold=max_threshold, target=target) #print("Low Variance Variables to drop", vars2drop_lv)
    train_cp_lv, test_cp_lv = apply_feature_selection(train, test, vars2drop_lv) #, filename=f"data/{file_tag}", tag="lowvar"
    
    vars2drop_rv: list[str] = select_redundant_variables(train, min_threshold=min_threshold, target=target) #print("Redundant Variables to drop", vars2drop_rv)
    train_cp_rv, test_cp_rv = apply_feature_selection(train, test, vars2drop_rv) #, filename=f"data/{file_tag}", tag="redundant"
    
    print("Original variables", train.columns.to_list()) #print("Original variables", train.columns.values)
    print(f"Original data: train={train.shape}, test={test.shape}")
    print(f"After low variance FS: train_cp={train_cp_lv.shape}, test_cp={test_cp_lv.shape}, vars2drop={vars2drop_lv}")
    print(f"After Redundant FS: train_cp={train_cp_rv.shape}, test_cp={test_cp_rv.shape}, vars2drop={vars2drop_rv}")
    
    return train_cp_lv, test_cp_lv, train_cp_rv, test_cp_rv
train: DataFrame = read_csv("data/stroke_train.csv"); test: DataFrame = read_csv("data/stroke_test.csv"); file_tag = "stroke"; target = "stroke" #eval_metric = "recall"
train_fs_lv, test_fs_lv, train_fs_rv, test_fs_rv = feature_selection(train, test, max_threshold=1.2, min_threshold=0.5, file_tag="stroke", target="stroke") # Depois da análise, escolhem-se os parametros finais mais adequados para seguir para próximos passos. #feature_selection(train, test, max_threshold=2, min_threshold=0.25, file_tag="stroke", target="stroke")

# Feature Extraction 
def feature_extraction(data: DataFrame, target: str = "class", n_components: int = 10):
    # PCA
    df = data.copy(deep=True)
    plot_multi_scatter_charts(data, [], target) #plot_multi_scatter_chart(data, var1="age", var2="bmi", var3="stroke")
    
    target_data: Series = df.pop(target)
    index: Index = df.index
    
    pca = PCA(n_components=n_components) #from sklearn.decomposition import PCA
    pca.fit(df)
    
    xvalues: list[str] = [f"PC{i+1}" for i in range(len(pca.components_))]
    ax = plot_bar_chart(xvalues, pca.explained_variance_ratio_, title="Explained variance ratio", xlabel="PC", ylabel="ratio", percentage=True, show_plot=False)
    plot_line_chart(xvalues, pca.explained_variance_ratio_, ax=ax, percentage=True)
    
    transf: PCA = pca.transform(df)
    data_trsf = DataFrame(transf, columns=xvalues, index=index)
    data_trsf: DataFrame = concat([data_trsf, target_data], axis=1)
    data_trsf.name = "Feature Extraction PCA transformation"
    plot_multi_scatter_charts(data_trsf, [], target) #plot_multi_scatter_chart(data_trsf, "PC1", "PC2", target)
    
    plot_multi_boxplots([data, data_trsf])
    return data_trsf
data: DataFrame = read_csv("data/stroke_scaled_zscore.csv", index_col="id"); data.name = "Z-score Scaling"
data_fe_trsf = feature_extraction(data, target=target, n_components=6)
# Perceber melhor qual o número de components que se estão a escolher

# y: ndarray = data_trsf.pop(target).to_list()
# X: ndarray = data_trsf.values
# trnX, tstX, trnY, tstY = train_test_split(X, y, train_size=0.7, random_state=42, stratify=y)
# train: DataFrame = concat([DataFrame(trnX, columns=data.columns), DataFrame(trnY, columns=[target])], axis=1) #train.to_csv(f"data/{file_tag}_train.csv", index=False)
# test: DataFrame = concat([DataFrame(tstX, columns=data.columns), DataFrame(tstY, columns=[target])], axis=1)
# plot_multi_bar_chart(["NB", "KNN"], evaluate_approach(train.copy(), test.copy(), target=target, metric="recall"), title= "PCA", percentage=True)



# Feature Generation
def feature_generation(data: DataFrame, q_vars: list[str] = [], sq_vars: list[str] = [], sqr_vars: list[str] = [], log_vars: list[str] = [], ):
    # Feature Generation (Variable generation) 
    # Criação de novas variáveis a partir das disponíveis
    
    df: DataFrame = data.copy(deep=True)
    vars: list[str] = list(set(q_vars + sq_vars + log_vars))
    d_vars: dict[str, list] = {var: [] for var in vars} # É mais fácil receber este dicionário como entrada do que receber cada lista de variáveis individualmente
    
    # Transformações
    
    # Quociente/Racional: 1/x ou 1/(1+x) ou x/(1+x)
    if q_vars != []:
        for var in q_vars:
            new_var = var + "_inv"
            # df[new_var] = 1.0 / df[var].replace(0, np.nan) 
            df[new_var] = np.where(df[var] == 0, np.nan, 1 / df[var]) # Beside the drop funnction several other modifiers are provided by the DataFrame class. add/div/mul/sub functions that compute the addition/division/product/subtraction between two dataframes, creating a new one, are examples of useful ones.
            d_vars[var].append(new_var)
    
    # Polinomiais: Square, cube, square root, etc. -> Fazer receber o expoente como entrada (de alguma forma)
    if sq_vars != []:
        for var in sq_vars:
            new_var = var + "_sq"
            df[new_var] = np.power(df[var], 2) # df[new_var] = df[var].mul(df[var], axis = 0) # df[new_var] = df[var] ** (1/2) 
            d_vars[var].append(new_var)
    
    # Fazer para square_root
    if sqr_vars != []:
        for var in sq_vars:
            new_var = var + "_sqr"
            df[new_var] = np.power(df[var], 1/2) # df[new_var] = df[var].mul(df[var], axis = 0) # df[new_var] = df[var] ** 2 
            d_vars[var].append(new_var)
    
    # Logaritmo/Exponencial: log/exp (Usar log(x+1) ou preencher com nan quando há presença de zeros) -> Receber a base, caso contrário usar logaritmo natural
    if log_vars != []:
        for var in log_vars:
            new_var = var + "_log"
            df[new_var] = np.log(df[var].replace(0, np.nan))
            d_vars[var].append(new_var)
    
    
    # FALTA FAZER:
    # Polinomiais (as restantes)
    # Módulo: |x| -> abs(x)
    # Funções trignométricas #sin_vars: list[str] = [], cos_vars: list[str] = [], tan_vars: list[str] = [] 
    # Diferenciação/Integração #diff_vars: list[str] = [], int_vars: list[str] = []
    # Z-score/Min-max/Rank-percentil/Quantil transform -> Feito no scaling (z-score e min-max)
    # Múltiplas interações entre variáveis através de diferentes combinações entre as mesmas e as respetivas operações associadas entre as mesmas (multiplicação/divisão, soma/subtração)
    
    
    # Reordenar colunas do dataframe
    cols = list(data.columns)
    for var in vars:
        pos = cols.index(var) # Isto não funciona se houver variáveis com o mesmo nome -> Só funciona se todas as variáveis tiverem nomes diferentes
        for i, new_var in enumerate(d_vars[var].keys()):
            cols.insert(pos + i + 1, new_var) #df.insert(df.columns.get_loc(var) + 1, new_var, df[var] ** 2) # Para ficar ao lado da variável original (Mas não funciona se forem aplicadas outras transformações à mesma variável -> Necessário reorganizar as colunas de outra forma no final)
    df = df[cols]
    
    return df

















# Methodology

from typing import Callable
#from dslabs_functions import CLASS_EVAL_METRICS, run_NB, run_KNN
from sklearn.naive_bayes import _BaseNB, GaussianNB, MultinomialNB, BernoulliNB
from sklearn.neighbors import KNeighborsClassifier

# eval_metrics = list(CLASS_EVAL_METRICS.keys())
CLASS_EVAL_METRICS: dict[str, Callable] = {"accuracy": accuracy_score, "recall": recall_score, "precision": precision_score, "auc": roc_auc_score, "f1": f1_score} #from sklearn.metrics import accuracy_score, recall_score, precision_score, roc_auc_score, f1_score


def run_NB(trnX, trnY, tstX, tstY, metric: str = "accuracy") -> dict[str, float]:
    estimators: dict[str, GaussianNB | MultinomialNB | BernoulliNB] = {"GaussianNB": GaussianNB(), "BernoulliNB": BernoulliNB()} #, "MultinomialNB": MultinomialNB(),
    best_model: GaussianNB | MultinomialNB | BernoulliNB = None  # type: ignore
    best_performance: float = 0.0
    eval: dict[str, float] = {}
    
    for clf in estimators:
        estimators[clf].fit(trnX, trnY)
        prdY: ndarray = estimators[clf].predict(tstX)
        performance: float = CLASS_EVAL_METRICS[metric](tstY, prdY)
        if performance - best_performance > DELTA_IMPROVE:
            best_performance = performance
            best_model = estimators[clf]
    if best_model is not None:
        prd: ndarray = best_model.predict(tstX)
        for key in CLASS_EVAL_METRICS:
            eval[key] = CLASS_EVAL_METRICS[key](tstY, prd)
    return eval
def run_KNN(trnX, trnY, tstX, tstY, metric="accuracy") -> dict[str, float]:
    kvalues: list[int] = [1] + [i for i in range(5, 26, 5)]
    best_model: KNeighborsClassifier = None  # type: ignore
    best_performance: float = 0
    eval: dict[str, float] = {}
    for k in kvalues:
        clf = KNeighborsClassifier(n_neighbors=k, metric="euclidean")
        clf.fit(trnX, trnY)
        prdY: ndarray = clf.predict(tstX)
        performance: float = CLASS_EVAL_METRICS[metric](tstY, prdY)
        if performance - best_performance > DELTA_IMPROVE:
            best_performance = performance
            best_model: KNeighborsClassifier = clf
    if best_model is not None:
        prd: ndarray = best_model.predict(tstX)
        for key in CLASS_EVAL_METRICS:
            eval[key] = CLASS_EVAL_METRICS[key](tstY, prd)
    return eval
def evaluate_approach(train: DataFrame, test: DataFrame, target: str = "class", metric: str = "") -> dict[str, list]: #metric: str = "accuracy"
    # The sequence of tasks # Processing each task
    train = train.copy(deep=True)
    test = test.copy(deep=True)
    
    trnY = train.pop(target).values
    trnX: ndarray = train.values
    tstY = test.pop(target).values
    tstX: ndarray = test.values
    
    if metric != "":
        eval_NB: dict[str, float] = run_NB(trnX, trnY, tstX, tstY, metric=metric)
        eval_KNN: dict[str, float] = run_KNN(trnX, trnY, tstX, tstY, metric=metric)
        eval = {met: {"NB": eval_NB[met], "KNN": eval_KNN[met]} for met in CLASS_EVAL_METRICS if eval_NB != {} and eval_KNN != {}}
        return eval
    else:
        rows, cols = len(CLASS_EVAL_METRICS), 2
        fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 3, rows * HEIGHT), squeeze=False) #dpi=300
        #fig.suptitle("Nr of standard and non-standard outliers per variable")
        i, j = 0, 0
        for i, metric in enumerate(CLASS_EVAL_METRICS):
            eval_NB: dict[str, float] = run_NB(trnX, trnY, tstX, tstY, metric=metric) #eval_NB: dict[str, float] | None = run_NB(trnX, trnY, tstX, tstY, metric=metric)
            eval_KNN: dict[str, float] = run_KNN(trnX, trnY, tstX, tstY, metric=metric) #eval_KNN: dict[str, float] | None = run_KNN(trnX, trnY, tstX, tstY, metric=metric)
            
            eval1 = {met: {"NB": eval_NB[met], "KNN": eval_KNN[met]} for met in CLASS_EVAL_METRICS if eval_NB != {} and eval_KNN != {}} #eval: dict[str, list] = {} # if eval_NB != {} and eval_KNN != {}: #     for met in CLASS_EVAL_METRICS: #         eval[met] = [eval_NB[met], eval_KNN[met]]
            eval2 = {"NB": {met: eval_NB[met] for met in CLASS_EVAL_METRICS if eval_NB != {} and eval_KNN != {}}, "KNN": {met: eval_KNN[met] for met in CLASS_EVAL_METRICS if eval_NB != {} and eval_KNN != {}}}
            
            plot_multi_bar_chart([metric for metric in CLASS_EVAL_METRICS], eval2, ax=axs[i,0], title=f"{file_tag} evaluation (metric={metric})", percentage=True, show_plot=False) #savefig(f"images/{file_tag}_eval.png")
            plot_multi_bar_chart(["NB", "KNN"], eval1, ax=axs[i,1], title=f"{file_tag} evaluation (metric={metric})", percentage=True, show_plot=False) #savefig(f"images/{file_tag}_eval.png")
        #return eval # Dá para guardar os results num dicionário depois
        show()

train: DataFrame = read_csv("data/stroke_train.csv"); test: DataFrame = read_csv("data/stroke_test.csv"); file_tag = "stroke"; target = "stroke"
evaluate_approach(train, test, target=target) #eval: dict[str, list] = evaluate_approach(train, test, target=target, metric="recall")




