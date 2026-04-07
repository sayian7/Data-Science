
# PROFILING

def get_variable_missing_values(data: DataFrame, show_plot: bool = False):
    # Missing values: Using the function for creating a bar chart, it is easy to see how many missing values there are for each variable. Note that with the if (in the 5th line) we only collect the variables with missing values.
    mv: dict[str, int] = {var: data[var].isna().sum() for var in data.columns} # Nr records with missing values per variable #mv: dict[str, int] = {var: data_cancer[var].isna().sum() for var in data_cancer.columns if data_cancer[var].isna().sum() > 0}
    nmv: dict[str, int] = {var: len(data[var]) - data[var].isna().sum() for var in data.columns}
    mv_p = {x: (mv[x]/data.shape[0])*100 for x in mv.keys()} # Percentage of missing values per variable
    nmv_p = {x: (nmv[x]/data.shape[0])*100 for x in mv.keys()} # Percentage of non missing values per variable
    if show_plot:
        rows, cols = 2, 1
        fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 3, rows * HEIGHT), squeeze=False) #dpi=300
        #fig.suptitle("Missing values")
        #plot_bar_chart(list(mv.keys()), list(mv.values()), ax=axs[1, 0], title="N.º of Missing values per variable", xlabel="Variables", ylabel="N.º of missing values", show_plot=False)
        plot_multi_bar_chart(list(mv.keys()), [Series(list(nmv.values()), name="Non Missing"), Series(list(mv.values()), name="Missing")], ax=axs[0, 0], title="Missing values per variable", xlabel="Variables", ylabel="Frequency", stacked=True, show_plot=False) #df_mv = Series(mv, index=mv.keys(), name='Missing values per variable') #df_mv.index.name = 'Variables'
        plot_bar_chart(list(mv_p.keys()), list(mv_p.values()), ax=axs[1, 0], title="Percentage of Missing values per variable", xlabel="Variables", ylabel="Percentage of missing values", percentage=True, show_plot=False)
        #plot_multi_bar_chart(list(mv_p.keys()), [Series(list(nmv_p.values()), name="Non Missing"), Series(list(mv_p.values()), name="Missing")], ax=axs[0, 1], title="Percentage of Missing values per variable", xlabel="Variables", ylabel="Percentage", show_plot=True) #df_mvp = Series(mv_p, index=mv_p.keys(), name='Missing values % per variable') #df_mvp.index.name = 'Variables'
    return mv #, nmv, mv_p, nmv_p
def get_variable_types(df: DataFrame, var_type: str = "", show_plot: bool = False) -> dict[str, list]:
    variable_types: dict = {"numeric": [], "binary": [], "date": [], "symbolic": []}
    nr_values: Series = df.nunique(axis=0, dropna=True)
    for c in df.columns:
        unique_vals = df[c].dropna().unique()
        if nr_values[c] == 2: variable_types["binary"].append(c); df[c].astype("bool")
        else:
            if all([isinstance(x, datetime) for x in unique_vals]): variable_types["date"].append(c) #df[c] = to_datetime(df[c], errors="raise")
            elif all([isinstance(x, int | float | numbers.Number | np.integer | np.float_) for x in unique_vals]): variable_types["numeric"].append(c) #to_numeric(df[c], errors="raise")
            elif all([isinstance(x, str | np.str_ | np.character) for x in unique_vals]): variable_types["symbolic"].append(c)
    if show_plot:
        n_vt: dict[str, int] = {tp: len(variable_types[tp]) for tp in variable_types.keys()}
        plot_bar_chart(n_vt, n_vt, title="N.º of variables per variable type", xlabel="Variable types", ylabel="Nº. of variables", show_plot=show_plot)
    return variable_types[var_type] if var_type in variable_types.keys() else variable_types

def print_summary_statistics(data: DataFrame):
    summary5: DataFrame = data.describe(include="all") # Descriptive Summary Statistics
    
    print(f"Dataset Dimensionality: Nr of records = {data.shape[0]} : Nr of variables = {data.shape[1]}")
    plot_bar_chart(["N.º of Records", "N.º of Variables"], list(data.shape), title="N.º of records vs N.º of variables")  #values: dict[str, int] = {"N.º Records": data_cancer.shape[0], "N.º Variables": data.data_cancer[1]}
    
    # TIME SERIES
    if get_variable_types(DataFrame(data.index), var_type="date", show_plot=False) != {}: print("First timestamp", data.index[0]); print("Last timestamp", data.index[-1]) 
    
    variable_types: dict[str, list] = get_variable_types(data, show_plot=True)
    counts: dict[str, int] = {tp: len(variable_types[tp]) for tp in variable_types.keys()}
    mv: dict[str, int] = get_variable_missing_values(data, show_plot=True) #{var: data[var].isna().sum() for var in data.columns} # Nr records with missing values per variable
    
    for tp in variable_types:
        if tp == "numeric" and variable_types[tp] != []:
            print(f"\n===== NUMERIC VARIABLES ({counts[tp]}) =====") #print(f"\nNumeric vars: {counts[tp]} : {variable_types[tp]}")
            table = {}
            for var in variable_types[tp]:
                table[var] = {
                    "Type": data[var].dtype,
                    "Count": summary5[var]["count"],
                    "Missings": mv[var],
                    "Mean": round(summary5[var]["mean"], 2),
                    "StdDev": round(summary5[var]["std"], 2),
                    "Min": summary5[var]["min"],
                    "Q1": summary5[var]["25%"],
                    "Median": round(summary5[var]["50%"], 2),
                    "Q3": summary5[var]["75%"],
                    "Max": summary5[var]["max"],
                }
                # print(f"\n{var}:") # var: str = "age"
            df_numeric = DataFrame(table)
            with pd.option_context('display.max_columns', None, 'display.width', None):
                print(df_numeric)
        
        elif tp == "binary" and variable_types[tp] != []:
            print(f"\n===== BINARY VARIABLES ({counts[tp]}) =====") #print(f"\nBinary vars: {counts[tp]} : {variable_types[tp]}")
            table = {}
            for var in variable_types[tp]:
                table[var] = {
                    "Type": data[var].dtype,
                    "Count": summary5[var]["count"],
                    "Missings": mv[var],
                    "Values": list(data[var].dropna().unique()),
                }
                # print(f"\n{var}:") # var: str = "gender"
                #print("\tUnique: ", summary5[var]["unique"])
                #print("\tTop: ", summary5[var]["top"])
                #print("\tFreq: ", summary5[var]["freq"])
            df_binary = DataFrame(table)
            with pd.option_context('display.max_columns', None, 'display.width', None):
                print(df_binary)
        
        elif tp == "symbolic" and variable_types[tp] != []:
            print(f"\n===== SYMBOLIC VARIABLES ({counts[tp]}) =====") #print(f"\nSymbolic vars: {counts[tp]} : {variable_types[tp]}")
            table = {}
            for var in variable_types[tp]:
                table[var] = {
                    "Type": data[var].dtype,
                    "Count": summary5[var]["count"],
                    "Missings": mv[var],
                    "Unique": summary5[var]["unique"],
                    "Values": list(data[var].dropna().unique()),
                    "Top": summary5[var]["top"],
                    "Freq": summary5[var]["freq"],
                }
                # print(f"\n{var}:") # var: str = "season"
            df_symbolic = DataFrame(table)
            with pd.option_context('display.max_columns', None, 'display.width', None):
                print(df_symbolic)


# Ajustar a função para receber como entrada se o dataset é Time Series ou não -> Fazer receber o target caso seja
def profilling(datasets: list[DataFrame]):
    for dataset in datasets:
        print_summary_statistics(dataset)
        plot_multi_line_charts(dataset) # Só faz sentido fazer este gráfico se o dataset for time series
        plot_scatter_charts(dataset)
        plot_boxplots(dataset)
        plot_outliers_count(dataset)
        plot_histograms(dataset)
        plot_correlation(dataset)

























def dataframe_operations(data: DataFrame):
    print("\nData type: ", type(data)) 
    print("\nShape:\n", "Records: ", data.shape[0], "Variables: ", data.shape[1])
    print("\nVariables:\n", data.columns.to_list())
    print("\nIndex:\n", data.index)
    print("\nRecords: \n", data.values, "\n")
    print(data.dtypes) # Variables types/formats 
    
    print("\n", data.head()) #n=3
    print("\n", data.tail(), "\n")
    
    # Criar/carregar e exportar dados
    pd.DataFrame(); pd.read_csv(); pd.read_json(); pd.to_csv(); pd.to_excel()
    
    # Explorar/Entender os datasets
    df.shape; df.columns; df.index
    df.info(); df.describe()
    df.head(); df.tail(); df.sample()
    
    
    
    # Seleção/Filtragem
    df['col']; df[['col1', 'col2']]
    df.loc[] # Coluna
    df.iloc[] # Linha
    df.querry() # filtros com sintaxe tipo SQL
    df.filter() # Filtrar colunas por nome
    df[df['col'] > 10] # Exemplo
    
    # data_cancer["age"] # Column
    # data_cancer.loc[9046] # Row
    # data_cancer.loc[9046, "age"]; data_cancer["age"].loc[9046]; data_cancer["age"][9046] # Record
    #list(map(list, data_cancer.to_numpy())) # values to get the data recorded as a two-dimensional table, a numpy.ndarray. The same can be obtained using the to_numpy method.
    
    
    
    
    
    #data.unique()
    print(data.nunique())
    #data.dropna()
    
    print(data.describe(include="all")) #summary5: DataFrame = data.describe(include="all") # Descriptive Summary Statistics
    
    for var in data.columns:
        if isinstance(data[var].dtype, np.float64):
            print(data[var].unique())
            print(data[var].nunique())
            print(data[var].mean()) #mean/std/mode/min/max
            print(data[var].nlargest()) #nlargest/nsmallest
    
    data_subset: DataFrame = data.sample(frac=0.05, replace=False) # Don't forget the replace parameter in order to get a different object, without loosing the original one. Instead of using the frac parameter, which defines the percentage of rows to collect, we can use n to specify the absolute number of records.
    data_subset: DataFrame = data.sample(n=5, replace=False)
    
    if False:
        data_algae_num: DataFrame = data_algae.drop(columns=["fluid_velocity", "river_depth", "season"], inplace=False) # either the pop or the drop functions. While the first returns the data eliminated and the second ignores it.
        #data_algae_sq = data_algae.copy(); data_algae_num["O2_sq"] = data_algae_num["Oxygen"].mul(data_algae_num["Oxygen"], axis = 0) # Beside the drop funnction several other modifiers are provided by the DataFrame class. add/div/mul/sub functions that compute the addition/division/product/subtraction between two dataframes, creating a new one, are examples of useful ones.
        data_algae_num["pH_label"] = data_algae.apply(lambda x: "acidic" if x["pH"] < 7 else "basic", axis=1) # The apply function is a general modifier able to apply a function to a dataframe or to a part of the dataframe. n the following example, we create a new column in the dataframe resulting from verifying if the pH is acidic or basic for each record in the data (established by the axis parameter).
        data_algae_symbolic: DataFrame = concat([data_algae[["fluid_velocity","river_depth","season"]], data_algae_num["pH_label"]], axis=1) # Another useful function is the concat function available in the pandas package. It receives any number of dataframes and create another one. It can append new records to a previous dataframe, or joining more columns to it, if they share the same index, the secret resides on the axis parameter: if it is assigned 
        #data_algae_symbolic.to_csv("data/algae_labeled.csv", header=True, index=True) # The last function we want to mention is the to_csv function, which is able to create a new csv file. It is a method of the DataFrame class, and receives the file name to be written, and if the index shall be considered or not (True/False).
        
        


data_demand.pivot_table(index="SKU", columns="Store", values="Sold Qty", aggfunc="sum", fill_value=0)


df_agg = data_demand.groupby([data_demand.index, "SKU"]).agg(sum)

df[var].cumsum() # Cumulativo

data_supply_demand.fillna(0, inplace=True)

# data.columns = data_population.columns.str.strip()


df_melted = df.melt(var_name="Coluna_Original", value_name="Valor") # Converter a matriz para formato de tabela com duas colunas
df_melted = df_melted.dropna() # Remover células vazias
df_melted.to_clipboard()
#df_melted.to_excel("tabela_transformada.xlsx", index=False) # Salvar a nova tabela no Excel
#print(df_melted.head())  # Exibir as primeiras linhas para verificar




n = 6 # Nº de observações
cols = ['A','B','C','D']
dados = [ [ i for j, x in enumerate(cols) ] for i in range(n) ]
r = [ {k: dados[i][j] for j,k in enumerate(cols)}   for i in range(len(dados))]
d = [ dict(zip(cols, dados[i])) for i in range(len(dados)) ]
s = [ dict( [ (x,dados[i][j]) for j,x in enumerate(cols)   ] ) for i in range(len(dados)) ]
df = pd.DataFrame(r)




# AGREGAÇÃO POR PERIODOS
block_size = 7
supply_df["period_block"] = supply_df["period"] // block_size
supply_agg = (supply_df.groupby(["period_block", "Supplier", "SKU"], as_index=False).agg({"Supply_available": "sum", "Supply_used": "sum"}))
demand_agg = (demand_df.groupby(["period_block", "Store", "SKU"], as_index=False).agg({"Demand_available": "sum", "Demand_used": "sum"}))


# FUNÇÃO
def aggregate_by_period(df, period_col, group_cols, sum_cols, block_size):
    df = df.copy()
    df["period_block"] = df[period_col] // block_size
    agg = (df.groupby(["period_block"] + group_cols, as_index=False).agg({c: "sum" for c in sum_cols}))
    #agg["period_range"] = agg["period_block"].apply(lambda b: f"{b*block_size}-{b*block_size + block_size - 1}")
    return agg
supply_agg = aggregate_by_period(supply_df, period_col="period", group_cols=["Supplier", "SKU"], sum_cols=["Supply_available", "Supply_used"], block_size=5)





# Manipulação de colunas
df.rename() # Renomear colunas
df.assign() # Criar novas colunas
df.drop() # Remover colunas ou linhas
df.astype() # Mudar tipo de dados
df.apply() # Aplicar função por linha ou coluna
df.map(); df.replace() # Mapear valores

# Limpeza de dados
df.isna(); df.notna() # Detetar valores NaN
df.dropna() # Remover valores NaN
df.fillna() # Preencher valores NaN
df.duplicated() # Encontrar valores duplicados
df.drop_duplicates() # Remover valores duplicados

# Ordenar e agrupar
df.sort_values() # Ordenar por coluna
df.sort_index() # Ordenar pelo índice
df.groupby() # Agregações (importante)
df.groupby('categoria')['coluna'].sum() # Exemplo

# Combinar/construir DataFrames
pd.concat() # Empilhar DataFrames
pd.merge() # Juntar por chave
df.join() # Juntar pelo índice

# Estatística
df.mean(); df.sum(); df.min(); df.max()
df.value_counts()
df.corr()
df.nunique()

# Datas e tempo
pd.to_datetime()
df['date'].dt.year; df['date'].dt.month; df['date'].dt.day
df.resample() # Séries temporais

# Performance e utilidades
df.copy() # Evitar bugs chatos
df.memory_usage()
df.pipe() # Pipelines elegantes
df.eval() # Expressões rápidas





# LIXO
mv: dict[str, int] = get_variable_missing_values(data_cancer, show_plot=True)
variable_types: dict[str, list] = get_variable_types(data_cancer, show_plot=True) #n_vt: dict[str, int] = {tp: len(variable_types[tp]) for tp in variable_types.keys()} # Variables types
#symbolic: list[str] = variable_types["symbolic"] #data_cancer[symbolic] = data_cancer[symbolic].apply(lambda x: x.astype("category"))
#binary: list[str] = variable_types["binary"] #data_cancer[binary] = data_cancer[binary].apply(lambda x: x.astype("bool")) # Não efetuar esta operação para variáveis binárias

