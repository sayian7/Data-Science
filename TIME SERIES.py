
from copy import deepcopy

# from matplotlib.pyplot import plot, legend
from matplotlib.pyplot import setp
from matplotlib.gridspec import GridSpec

from dslabs_functions import FORECAST_MEASURES, DELTA_IMPROVE
from dslabs_functions import PAST_COLOR, FUTURE_COLOR, PRED_PAST_COLOR, PRED_FUTURE_COLOR

from statsmodels.tsa.seasonal import DecomposeResult, seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
from statsmodels.tsa.arima.model import ARIMA

from sklearn.base import RegressorMixin
from sklearn.linear_model import LinearRegression

from torch import no_grad, tensor
from torch.nn import LSTM, Linear, Module, MSELoss
from torch.optim import Adam
from torch.utils.data import DataLoader, TensorDataset










# TIME SERIES




# 1. Profiling


# 1. Dimensionality # Analysis # The data under analysis in this topic is a single variable time series, collected from the ASHRAE - Great Energy Predictor III challenge available on Kaggle. # As for tabular data, the first thing to understand is the data dimensionality. In the case of a single time series, it's simple - we are in the presence of one single dimension. But usually, in this context, dimensionality corresponds to the number of observations taken, which refers to the length of the series. # So after loading the data, the usual procedure is to plot the data at the most atomic granularity to look for regularities (repetitions) in the data.
plot_line_chart(data_ashrae.index, data_ashrae["meter_reading"], xlabel=data_ashrae.index.name, ylabel="meter_reading") #, title=f"{file_tag} hourly (target_var)" # Univariate Time Series # For plotting univariate time series, we can make use of the plot_line_chart available in the dslabs_functions, as done below.# The plot shows the electrical consumption of a specific building during the year of 2016, hourly measured, totalizing 8784 observations.# There are some interesting things we can see from looking at the chart: # 1. there are some time intervals where the consumption is constant and around 425 kWh; # 2. there is kind of a pattern that approximately repeats weekly; # 3. the series seems to show a small consumption reduction along the year.# This tells us that there should be some components, and analysing the series granularity is one of the ways to address it.
plot_line_charts(data_portugal_population) #plot_line_charts(data_ashrae) #plot_multi_line_chart(data_ashrae.index, {var: data_ashrae[var] for var in data_ashrae.columns}, xleftQ=True) #plot_ts_multivariate_chart(data_portugal, title=f"{file_tag} {target}" )# Multivariate Time Series # Não usar "plot_ts_multivariate_chart" mas sim o "plot_line_charts" # For plotting multivariate time series, we need a new function in order to represent each variable in its natural scale. Naturally, if all vars have similar ranges, we could use the plot_multiline_chart function, available in the dslabs_functions. #The plot_ts_multivariate_chart function defined below can be used in this case.
plot_multi_line_chart(data_portugal_population.index, {var: data_portugal_population[var] for var in data_portugal_population.columns})
plot_multi_line_chart(data_appliances.index, {var: data_appliances[var] for var in data_appliances.columns})
plot_multi_line_chart(data_algae.index, {var: data_algae[var] for var in data_algae.columns}) #data_algae.drop(columns=['fluid_velocity', 'river_depth', 'season'], inplace=True)


# 2. Granularity # Aggregation is just the operation of grouping smaller details into a coarser one, most similar to the approach we took in the profiling step. # In order to do it, we just need to apply the previous function "aggregation_by_date", already available in the dslabs_functions file, that receives the univariate series to transform, the granularity level to aggregate into - gran_level, and the aggregation function to apply - agg_func.
grans: list[str] = ["H", "D", "W", "M", "Q", "Y"] #"S", "M", 
grans_names: dict[str] = {g: ["Hour", "Day", "Week", "Month", "Quarter", "Year"][i] for i, g in enumerate(grans)} #"Second","Minute",
plot_multi_line_chart(data_ashrae.index, {g_name: aggregation_by_date(data_ashrae["meter_reading"], g, mean) for g, g_name in grans_names.items()})
#plot_line_chart(aggregation_by_date(data_ashrae["meter_reading"], "D").index, aggregation_by_date(data_ashrae["meter_reading"], "D"), xlabel=aggregation_by_date(data_ashrae["meter_reading"], "D").index.name, ylabel=target, title=f"{file_tag} daily mean {target}", xleftQ=True) # Aggregating by days, we perform a kind of a smoothing, since we are using the mean as aggregation function. And as a result, we found a smoother version of the original time series, with less noise. # In this new version, we continue to identify a cyclic behavior, which seems to be shown weekly. # ss_days: Series = aggregation_by_date(data_ashrae["meter_reading"], "D")
#plot_line_charts({grans_names[g]: aggregation_by_date(data_ashrae["meter_reading"], g, mean) for g in grans}, list(grans_names.values()), xleftQ=True) # title=f"granularity={grans[i]}" #plot_line_charts({g: aggregation_by_date(data_ashrae["meter_reading"], g, sum) for g in grans}, grans, xleftQ=True)# The chart for weekly consumption is quite different from the previous ones – it does not show any cyclic behavior as before! Indeed, despite the reduction trend on the second semester, the weekly consumptions are almost constant in the first quarter.# The chart for monthly consumptions confirm those identified trends… and confirms any suspicion about the lack of stationarity in the time series. Indeed its mean is not constant along time. In particular we identify very different values of consumption per month, but there are more formal ways to deal with that!


# 3. Data Distribution
plot_line_charts({g_name: aggregation_by_date(data_ashrae["meter_reading"], g, sum) for g, g_name in grans_names.items()}, list(grans_names.values())) #plot_multi_line_chart(data_ashrae.index, {grans_names[g]: aggregation_by_date(data_ashrae["meter_reading"], g, sum) for g in grans}, xleftQ=True)
plot_date_granularity_boxplots(data_ashrae); plot_date_granularity_histograms(data_ashrae) # In the histograms we recognize that our data follow approximately a normal distribution for the higher granularities. But the same doesn't happen for the lowest ones. Those histograms show a multimodal distribution, with at least two distinct modes.
plot_date_granularity_boxplots(data_appliances, show_summary=False); plot_date_granularity_histograms(data_appliances, show_summary=False)


# Autocorrelation
def lagged_series(series: Series, max_lag: int, delta: int = 1):
    # Esta função empurra valores para a frente, sendo que os últimos valores são eliminados (não são colocados esses valores em novos timestamps)
    # Necessário alterar esta função para reconhecer o significado de delta e max_lag -> Se é em dias, semanas, meses, quarters, anos, etc.
    lagged_series: dict = {"Original": series} #, "lag 1": series.shift(1)
    for i in range(delta, max_lag + 1, delta):
        lagged_series[f"Lag {i}"] = series.shift(i)
    return lagged_series
def plot_autocorrelation(series: Series, max_lag: int, delta: int = 1): 
    # Autocorrelation # For TIME SERIES only
    def lagged_series(series: Series, max_lag: int, delta: int = 1):
        lagged_series: dict = {"Original": series} #, "lag 1": series.shift(1)
        for i in range(delta, max_lag + 1, delta):
            lagged_series[f"Lag {i}"] = series.shift(i)
        return lagged_series
    k: int = int(max_lag / delta)
    fig = figure(figsize=(4 * HEIGHT, 2 * HEIGHT), constrained_layout=True)
    gs = GridSpec(2, k, figure=fig) #from matplotlib.pyplot import setp #from matplotlib.gridspec import GridSpec
    lag_series = lagged_series(series=series, max_lag=max_lag, delta=delta)
    del lag_series["Original"]
    for i, lag_name in enumerate(lag_series):
        ax = fig.add_subplot(gs[0, i])
        plot_scatter_chart(lag_series[lag_name], series, title=f"{lag_name} x Original", xlabel=f"{lag_name}", ylabel="Original", ax=ax, xleftQ=True, yleftQ=True, show_plot=False)
    ax = fig.add_subplot(gs[1, :])
    ax.acorr(series, maxlags=max_lag)
    ax.set_title("Autocorrelation"); ax.set_xlabel("Lags")
    show()
plot_multi_line_chart(data_ashrae.index, lagged_series(data_ashrae["meter_reading"], max_lag=500, delta=250), xlabel=data_ashrae.index.name, ylabel="meter_reading") #plot_line_charts(DataFrame(lagged_series(data_ashrae["meter_reading"], max_lag=500, delta=250))) #plot_multi_line_chart(algae.index, lagged_series(algae, max_lag=50, delta=25), xlabel=algae.index.name, ylabel="pH") #plot_line_charts(DataFrame(lagged_series(algae, max_lag=50, delta=25)))
plot_autocorrelation(data_ashrae["meter_reading"], max_lag=100, delta=20) 


# 4. Stationarity
def eval_stationarity(series: Series) -> bool:
    # Stationarity # Augmented Dickey-Fuller test # But there more precise ways to do it! The Augmented Dickey-Fuller test is a statistical test widely used to verify the stationarity of a series. It determines how strongly a time series is defined by a trend: if this is true, then the series is non-stationary. # In this manner, we have two cases: # p-value <= 0.05 : the series is stationary, meaning its values do not depend on time; # p-value > 0.05 : the series is non-stationary, meaning it shows a time-dependent structure. # This test is implemented in the statsmodels.tsa.stattools package through the adfuller function, which returns a dictionary with ********____********.
    result = adfuller(series) #from statsmodels.tsa.stattools import adfuller
    print(f"ADF Statistic: {result[0]:.3f}")
    print(f"p-value: {result[1]:.3f}")
    print("Critical Values:")
    for key, value in result[4].items():
        print(f"\t{key}: {value:.3f}")
    print(f"The series {'is' if (result[1] <= 0.05) else 'is not'} stationary") #return result[1] <= 0.05
def plot_series_components(series: Series, title: str = "", xlabel: str = "time", ylabel: str = "") -> list[Axes]:
    # Seasonality # The statsmodels.tsa.seasonal package provides the seasonal_decompose function, which returns a DecomposeResult object, that we can plot to better understand the seasonality of a time series.
    # In order to make it simppler to plot those results we implemented the plot_time_series_components.
    decomposition: DecomposeResult = seasonal_decompose(series, model="add") #from statsmodels.tsa.seasonal import DecomposeResult, seasonal_decompose
    components: dict = {"observed": series, "trend": decomposition.trend, "seasonal": decomposition.seasonal, "residual": decomposition.resid}
    rows: int = len(components)
    fig: Figure
    axs: list[Axes]
    fig, axs = subplots(rows, 1, figsize=(3 * HEIGHT, rows * HEIGHT), squeeze=False)
    #fig.suptitle(f"{title}")
    i: int = 0
    for i, key in enumerate(components):
        plot_line_chart(components[key].index, components[key], ax=axs[i, 0], title=key, xlabel=xlabel, ylabel=ylabel, show_plot=False)
    show()
    eval_stationarity(series)
    return axs
def plot_series_mean_lines(series: Series, max_bins: int = 1, delta_bins: int = 1, show_all: bool = True) -> list[Axes]: #, title: str = "", xlabel: str = "time", ylabel: str = ""
    bins: list[int] = [1] + list(range(delta_bins, max_bins + 1, delta_bins))
    n: int = len(series)
    rows: int = len(bins)
    cols: int = 1
    fig: Figure
    axs: list[Axes]
    if show_all: fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 3, rows * HEIGHT), squeeze=False)
    mean_lines: dict[str] = {}
    for i, n_bins in enumerate(bins):
        mean_line: list[float] = []
        for i_bin in range(n_bins):
            segment: Series = series[i_bin * n // n_bins : (i_bin + 1) * n // n_bins]
            mean_value: list[float] = [segment.mean()] * (n // n_bins)
            mean_line += mean_value
        mean_line += [mean_line[-1]] * (n - len(mean_line))
        mean_lines[f"mean (bins={n_bins})"] = mean_line
        if show_all: plot_multi_line_chart(series.index, [series, Series(mean_line, index=series.index, name=f"mean (bins={n_bins})")], ax=axs[i,0], title=f"{file_tag} stationary study (bins={n_bins})", xlabel=series.index.name, ylabel=series.name, show_plot=False) 
        #plot_multi_line_chart(ashrae.index, [ashrae, Series([ashrae.mean()] * len(ashrae), name="mean")], xlabel=ashrae.index.name, ylabel=target, title=f"{file_tag} stationary study", xleftQ=True) #plot_line_chart(ashrae.index, ashrae, xlabel=ashrae.index.name, ylabel=target, title=f"{file_tag} stationary study", name="original", xleftQ=True) #plt.plot(ashrae.index, [ashrae.mean()] * n, "r-", label="mean")
        #plot_line_chart(ashrae.index, ashrae, xlabel=ashrae.index.name, ylabel=target, title=f"{file_tag} stationary study", name="original", show_stdev=True) #plot(ashrae.index, mean_line, "r-", label="mean")
    if show_all: show()
    plot_multi_line_chart(series.index, [series]+[Series(mean_lines[i], index=series.index, name=i) for i in mean_lines], title=f"{file_tag} stationary study (bins={n_bins})", xlabel=series.index.name, ylabel=series.name, show_plot=True) 
    eval_stationarity(series)

eval_stationarity(data_ashrae["meter_reading"]) # From the results of the Augmented Dickey-Fuller test when applied to our consumption dataset, we perceive it as stationary.
plot_series_components(data_ashrae["meter_reading"], title=f"{file_tag} hourly {target}", xlabel=data_ashrae["meter_reading"].index.name, ylabel="meter_reading") # And now we just apply it to our time series.
plot_series_mean_lines(data_ashrae["meter_reading"], max_bins=50, delta_bins=10, show_all=False)




# 2. Transformation / Preparation


# 1. Scaling
data_ashrae_zscore_scaled, _ = scaling(data_ashrae, target="meter_reading", include_target=True, show_plot=True) # In order to see it in action, consider the ASHRAE dataset as before. # Note the vertical axes in both figures: now the data is centered on the zero, instead of ranging in the hundreds.
plot_line_charts(DataFrame({"Original": data_ashrae["meter_reading"], "Series after scalling": data_ashrae_zscore_scaled["meter_reading"]})) #plot_multi_line_chart(ashrae.index, {"Original": ashrae, "Series after scalling": ashrae_zscore_scaled}, xleftQ=True)

# 2. Smoothing
def smoothing(data: DataFrame, win_size: int = 10):
    # For time series only # 2. Smoothing
    df_smooth: DataFrame = data.rolling(window=win_size).mean(); #df_smooth.name = f" {series.name} Smooth size={win_size}"
    return df_smooth
def plot_series_smoothing_by_window_sizes(series: Series, max_win: int = 100, delta_win: int = 10):
    # Rolling mean
    win_sizes: list[int] = [1] + list(range(delta_win, max_win + 1, delta_win)) #[25, 50, 75, 100]
    fig: Figure
    axs: list[Axes]
    rows, cols = len(win_sizes), 1
    fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 3, rows * HEIGHT), squeeze=False)
    #fig.suptitle(f"{file_tag} {target} after smoothing")
    smoothed_series: dict[str] = {}
    for i, win_size in enumerate(win_sizes):
        ss_smooth: Series = series.rolling(window=win_size).mean()
        smoothed_series[f"Smooth size={win_size}"] = ss_smooth
        plot_line_chart(ss_smooth.index, ss_smooth, ax=axs[i,0], title=f"{file_tag} {target} after smoothing (size={win_size})", xlabel=ss_smooth.index.name, ylabel=target, show_plot=False)
    show()
    plot_multi_line_chart(series.index, smoothed_series, title=f"{file_tag} {target} after smoothing", xlabel=series.index.name, ylabel=target)
plot_series_smoothing_by_window_sizes(data_ashrae["meter_reading"], max_win=100, delta_win=25)
data_ashrae_smoothed = smoothing(data_ashrae["meter_reading"], win_size=10)

# 3. Aggregation
def aggregation_by_var(data: Series | DataFrame, var: str = "", agg_func: str = "sum") -> Series | DataFrame:
    df: Series | DataFrame = data.copy(deep=True) # 2. Granularity
    df = df.groupby(by=df[var], dropna=True, sort=True).agg(agg_func) if isinstance(var, str) else df.groupby(by=df.index, dropna=True, sort=True).agg(agg_func)
    return df
def aggregation_by_date(data: Series | DataFrame, gran_level: str = "D", gran_level2: int = 1, agg_func: str = "mean") -> Series | DataFrame:
    # Granularity # We use the function "aggregation_by_date" instead of "ts_univariate_aggregation_by" function to do that. # Let's look at the AHSRAE data used before. # We've already perceived that data is recorded hourly, but we can try other aggregations...  # Esta função muito provavelmente tem erros de agregação quando os intervalos não são completamente divisiveis -> Ver como foi feito no projeto para contornar este problema
    # For time series only
    df: Series | DataFrame = data.copy(deep=True)
    grans: list[str] = ["H", "D", "W", "M", "Q", "Y"] #"S", "M", 
    grans_names: dict[str] = {g: ["Hour", "Day", "Week", "Month", "Quarter", "Year"][i] for i, g in enumerate(["H", "D", "W", "M", "Q", "Y"])} #"Second", "Minute",
    
    if gran_level in grans_names: 
        if gran_level2 == 1:
            index: Index[Period] = df.index.to_period(gran_level)
            df = df.groupby(by=index, dropna=True, sort=True).agg(agg_func)
            df.index.drop_duplicates()
            df.index = df.index.to_timestamp()
            df.index.name = grans_names[gran_level]
        else:
            #grans2: list[str] = [1, 2, 3, 5, 10] # Tanto podem ser anos como outra coisa qualquer -> Necessário específicar o tipo de gran (Year, Month, Day, Hour, etc.)
            #grans_names2: dict[str] = {g: ["One-Year", "Two-Year", "Three-Year", "Five-Year", "Ten-Year"][i] for i, g in enumerate([1, 2, 3, 5, 10])}
            # df = df.groupby(by = ((data.index.year - data.index[0].year) // gran_level2), dropna=True, sort=True).agg(agg_func) #df = df.groupby(by=(df.index.year//gran_level)*gran_level, dropna=True, sort=True).agg(agg_func)
            # df.index = [data.index[0].year + gran_level2 * i for i in df.index]
            df = df.resample(f"{gran_level2}{gran_level}S").agg(agg_func) # "S" significa start (início do período).
            df.index.name = f"{gran_level2}-{grans_names[gran_level]}"
            #df.index = to_datetime(df.index, format='%Y')
            df.index.drop_duplicates()
            #print(df.head())
    return df
def plot_aggregation_by_date(data: DataFrame | Series, vars: list[str], grans_names: dict[str], agg_func: str = "mean", show_all: bool = False):
    if vars == []: vars = list(data.columns)
    rows, cols = len(vars), 1
    fig, axs = subplots(rows, cols, figsize=(cols * HEIGHT * 5, rows * HEIGHT), squeeze=False)
    for i, var in enumerate(vars):
        plot_multi_line_chart(data.index, {gran_name: aggregation_by_date(data[var], gran_level=g, agg_func=agg_func) for g, gran_name in grans_names.items()}, ax=axs[i,0], title=f"{var}", xlabel=data.index.name, ylabel=f"{var} Values", xleftQ=False, show_plot=False)
    show()
    for var in vars:
        plot_line_charts({gran_name: aggregation_by_date(data[var], gran_level=g, agg_func=agg_func) for g, gran_name in grans_names.items()}, list(grans_names.values()), xleftQ=True)
    if show_all:
        for g, gran_name in grans_names.items():
            plot_line_charts({var: aggregation_by_date(data[var], gran_level=g, agg_func=agg_func) for var in vars}, vars, xleftQ=True)

plot_line_charts({grans_names[g]: aggregation_by_date(data_ashrae["meter_reading"], g, sum) for g in grans}, list(grans_names.values()), xleftQ=True) #plot_line_chart(aggregation_by_date(series, gran_level="D", agg_func=sum).index, aggregation_by_date(series, gran_level="D", agg_func=sum), title=f"{file_tag} daily {target}", xlabel=aggregation_by_date(series, gran_level="D", agg_func=sum).index.name, ylabel=target)# Note, that instead of using the mean as the aggregation function, we used the sum instead. This is just to ensure that we do not loose any information. Remember that this is only possible when the variable to aggregate accepts such aggregation and keeps its semantics.# If our data were about bank accounts or temperatures, summing them along hours would result on wrong values.
plot_multi_line_chart(data_ashrae.index, {grans_names[g]: aggregation_by_date(data_ashrae["meter_reading"], g, mean) for g in grans}, xleftQ=True)

plot_line_charts(data_appliances) # Multivariate Time Series # Aggregating multivariate time series is also possible, and can be done through the previous function "aggregation_by_date" as well.
plot_aggregation_by_date(data_appliances, vars=[], grans_names=grans_names, agg_func=mean)
plot_aggregation_by_date(data_appliances, vars=[], grans_names=grans_names, agg_func=sum)


#plot_line_chart(ashrae.index, ashrae, xlabel=data.index.name, ylabel=target, title=f"{file_tag} hourly {target}") # Univariate Time Series
#plot_line_charts(data_appliances) #title=f"{file_tag} {target}" # Multivariate Time Series # And the same for multi-variated series...

# 5. Differentiation
def differentiation(data: DataFrame, n_diff: int = 1): # 5. Differentiation
    df_diff: DataFrame = data.copy(deep=True)
    for i in range(1, n_diff + 1):
        df_diff: DataFrame = df_diff.diff()
    return df_diff
def plot_differentiation(data: DataFrame, n_diff: int = 1, show_all: bool = True):
    #plot_line_chart(ss_diff.index, ss_diff, title="Differentiation", xlabel=ashrae.index.name, ylabel=target)
    #plot_line_charts(diff_df) #title=f"{file_tag} {target} - after first differentiation"
    diffs = {}
    for i in range(n_diff + 1):
        if i == 0: df_diff: DataFrame = data
        else: df_diff: DataFrame = df_diff.diff()
        diffs[i] = df_diff
        if show_all: plot_line_charts(df_diff) #title=f"Differentiation (n={i})" title=f"{file_tag} {target} - after first differentiation"    
    
    rows = len(data.columns)
    fig, axs = subplots(rows, 1, figsize=(HEIGHT * 5, rows * HEIGHT), squeeze=False)
    for i, var in enumerate(data.columns):
        plot_multi_line_chart(data[var].index, {(j,var): diffs[j][var] for j in diffs}, ax=axs[i, 0], show_plot=False)
    show()
    
    for i, var in enumerate(data.columns): plot_line_charts(DataFrame({i: df[var] for i, df in diffs.items()}))

differentiation(data_appliances, n_diff=2)
differentiation(data_ashrae, n_diff=2)

plot_differentiation(data_appliances, n_diff=2, show_all=False)
plot_differentiation(data_ashrae, n_diff=2)








# Forecasting

# Training
def series_train_test_split(data: Series, train_pct: float = 0.90) -> tuple[Series, Series]:
    # Training # The train of forecasting models follows the same principles as for classification. The first important thing is to split train from test data, which can be done through the series_train_test_split. Remember that in the temporal context, we need to split the data according to time, to ensure that no future data is used to train for predicting the past.
    train_size: int = int(len(data) * train_pct)
    df: Series = data.copy(deep=True)
    train: Series = df.iloc[:train_size, 0] #df.iloc[:train_size, :]
    test: Series = df.iloc[train_size:, 0]
    return train, test
def dataframe_train_test_split(data: DataFrame, trn_pct: float = 0.90) -> tuple[DataFrame, DataFrame]:
    trn_size: int = int(len(data) * trn_pct)
    df_cp: DataFrame = data.copy()
    train: DataFrame = df_cp.iloc[:trn_size]
    test: DataFrame = df_cp.iloc[trn_size:]
    return train, test

def plot_forecasting_series(train: Series, test: Series, prd_tst: Series, title: str = "", xlabel: str = "time", ylabel: str = "") -> list[Axes]:
    # Another important tool is for visualizing the series and its forecasting, preferably both the train and test portions. The function plot_forecasting_series does it using the colors chosen for it (PAST_COLOR, FUTURE_COLOR, PREDICTION_PAST_COLOR, PREDICTION_FUTURE_COLOR), that you can change to your preference.
    fig, ax = subplots(1, 1, figsize=(4 * HEIGHT, HEIGHT), squeeze=True)
    fig.suptitle(title)
    ax = set_chart_labels(ax=ax, xlabel=xlabel, ylabel=ylabel)
    
    xvalues = train.index.to_list() + test.index.to_list()
    yvalues = {"train": train, "test": test, "Predicted test": prd_tst}
    yvals = np.linspace(min([x for e in yvalues for x in yvalues[e] if not math.isnan(x)]), max([x for e in yvalues for x in yvalues[e] if not math.isnan(x)]), len(xvalues))
    ax = set_chart_xticks(xvalues, yvals, ax=ax) #percentage=percentage, xleftQ=xleftQ, yleftQ=yleftQ
    
    ax.plot(train.index, train.values, label="train", color=PAST_COLOR) #from dslabs_functions import PAST_COLOR, FUTURE_COLOR, PRED_PAST_COLOR, PRED_FUTURE_COLOR, HEIGHT
    ax.plot(test.index, test.values, label="test", color=FUTURE_COLOR)
    ax.plot(prd_tst.index, prd_tst.values, "--", label="test prediction", color=PRED_FUTURE_COLOR)
    ax.legend(prop={"size": 5})
    show() 
    #savefig(f"images/{file_tag}_simpleAvg_forecast.png")
    #savefig(f"images/{file_tag}_persistence_optim_forecast.png")
    #savefig(f"images/{file_tag}_persistence_real_forecast.png")
    #savefig(f"images/{file_tag}_exponential_smoothing_{measure}_forecast.png")
    #savefig(f"images/{file_tag}_rollingmean_{measure}_forecast.png")
    #savefig(f"images/{file_tag}_linear_regression_forecast.png")
    return ax
def plot_forecasting_eval(trn: Series, tst: Series, prd_trn: Series, prd_tst: Series, title: str = "") -> list[Axes]:
    # At last, we need to evaluate the quality of our model, which may be measured both by scale-dependent errors (RMSE and MAE) and percentage errors (MAPE), but also the R2, all available in the sklearn.metrics package in the regression measures section. Now available through the FORECAST_MEASURES in the dslabs_functions file.
    ev1: dict = {"RMSE": {"train": sqrt(FORECAST_MEASURES["MSE"](trn, prd_trn)), "test": sqrt(FORECAST_MEASURES["MSE"](tst, prd_tst))}, "MAE": {"train": FORECAST_MEASURES["MAE"](trn, prd_trn), "test": FORECAST_MEASURES["MAE"](tst, prd_tst)}} #from dslabs_functions import FORECAST_MEASURES
    ev2: dict = {"MAPE": {"train": FORECAST_MEASURES["MAPE"](trn, prd_trn), "test": FORECAST_MEASURES["MAPE"](tst, prd_tst)}, "R2": {"train": FORECAST_MEASURES["R2"](trn, prd_trn), "test": FORECAST_MEASURES["R2"](tst, prd_tst)}}
    #print(ev1, ev2)
    fig, axs = subplots(1, 2, figsize=(1.5 * HEIGHT, 0.75 * HEIGHT), squeeze=True)
    fig.suptitle(title)
    for i, (ev, title) in enumerate(zip([ev1, ev2], ["Scale-dependent error", "Percentage error"])):
        plot_multi_bar_chart(["train", "test"], ev, ax=axs[i], title=title, percentage=(i==1), show_plot=False)
    show()
    #savefig(f"images/{file_tag}_simpleAvg_eval.png")
    #savefig(f"images/{file_tag}_persistence_optim_eval.png")
    #savefig(f"images/{file_tag}_persistence_real_eval.png")
    #savefig(f"images/{file_tag}_exponential_smoothing_{measure}_eval.png") 
    #savefig(f"images/{file_tag}_rollingmean_{measure}_win{params[0]}_eval.png")
    #savefig(f"images/{file_tag}_linear_regression_eval.png")
    return axs



# 1. Simple Average
class SimpleAvgRegressor(RegressorMixin): #from sklearn.base import RegressorMixin
    # The Simple Average regressor is the easiest to implement, allways predicting the outcome to be the data mean value. For implementing it, we extend the sklearn class RegressorMixin, by redifining the fit and predict methods, as follows:
    def __init__(self):
        super().__init__()
        self.mean: float = 0.0
        return
    def fit(self, X: Series):
        self.mean = X.mean()
        return
    def predict(self, X: Series) -> Series:
        prd: list = len(X) * [self.mean]
        prd_series: Series = Series(prd)
        prd_series.index = X.index
        return prd_series

# 2. Persistence Model
class PersistenceOptimistRegressor(RegressorMixin): #from sklearn.base import RegressorMixin
    # The Persistence model just predicts the outcome to be the same as the last value seen. Again, for implementing it, we extended the sklearn class RegressorMixin, by redifining the fit and predict again.
    # Note that the more informed persistence model is the one that is able to predict just one step ahead - we call it the PersistenceOptimistRegressor and implement it as follows:
    def __init__(self):
        super().__init__()
        self.last: float = 0.0
        return
    def fit(self, X: Series):
        self.last = X.iloc[-1]
        # print(self.last)
        return
    def predict(self, X: Series):
        prd: list = X.shift().values.ravel()
        prd[0] = self.last
        prd_series: Series = Series(prd)
        prd_series.index = X.index
        return prd_series
class PersistenceRealistRegressor(RegressorMixin):
    # However, in order to the Persistence model to be comparable with the rest of estimators used by us, we need an implementation that looks ahead in the future, just using the training dataset and the model's predictions for the rest of the time. This is done through our second implementation named PersistenceRealistRegressor.
    def __init__(self):
        super().__init__()
        self.last = 0
        self.estimations = [0]
        self.obs_len = 0
    def fit(self, X: Series):
        for i in range(1, len(X)):
            self.estimations.append(X.iloc[i - 1])
        self.obs_len = len(self.estimations)
        self.last = X.iloc[len(X) - 1]
        prd_series: Series = Series(self.estimations)
        prd_series.index = X.index
        return prd_series
    def predict(self, X: Series):
        prd: list = len(X) * [self.last]
        prd_series: Series = Series(prd)
        prd_series.index = X.index
        return prd_series
# 4. Rolling Mean
class RollingMeanRegressor(RegressorMixin): #from sklearn.base import RegressorMixin
    # The Rooling Mean technique, uses a sliding window with size win and computes its mean value for predicting the next one. In order to implement it, we propose the RollingMeanRegressor class by extending the sklearn class RegressorMixin as before:
    def __init__(self, win: int = 3):
        super().__init__()
        self.win_size = win
        self.memory: list = []
    def fit(self, X: Series):
        self.memory = X.iloc[-self.win_size :]
        # print(self.memory)
        return
    def predict(self, X: Series):
        estimations = self.memory.tolist()
        for i in range(len(X)):
            new_value = mean(estimations[len(estimations) - self.win_size - i :])
            estimations.append(new_value)
            #print(i, new_value, estimations)
        prd_series: Series = Series(estimations[self.win_size :])
        prd_series.index = X.index
        return prd_series

# 3. Exponential Smoothing
def exponential_smoothing_study(train: Series, test: Series, measure: str = "R2"):
    # Exponential Smoothing is a simple model that we may say is between the Simple Average and the Persistence models. We are using its implementation from the statsmodels.tsa package - the
    # Since our regressor depends on one parameter - the , we need to study it, in order to find the best forecaster for our data. For that, we implement the function exponential_smoothing_study as follows.
    alpha_values = [i / 10 for i in range(1, 10)]
    flag = measure == "R2" or measure == "MAPE"
    best_model = None
    best_params: dict = {"name": "Exponential Smoothing", "metric": measure, "params": ()}
    best_performance: float = -100000
    
    yvalues = []
    for alpha in alpha_values:
        tool = SimpleExpSmoothing(train) #from statsmodels.tsa.holtwinters import SimpleExpSmoothing
        model = tool.fit(smoothing_level=alpha, optimized=False)
        prd_tst = model.forecast(steps=len(test))
        
        eval: float = FORECAST_MEASURES[measure](test, prd_tst) #from dslabs_functions import FORECAST_MEASURES, DELTA_IMPROVE
        # print(w, eval)
        if eval > best_performance and abs(eval - best_performance) > DELTA_IMPROVE:
            best_performance: float = eval
            best_params["params"] = (alpha,)
            best_model = model
        yvalues.append(eval)
    
    print(f"Exponential Smoothing best with alpha={best_params['params'][0]:.0f} -> {measure}={best_performance}")
    plot_line_chart(alpha_values, yvalues, title=f"Exponential Smoothing ({measure})", xlabel="alpha", ylabel=measure, percentage=flag)
    #savefig(f"images/{file_tag}_exponential_smoothing_{measure}_study.png")
    return best_model, best_params

# 4. Rolling Mean
def rolling_mean_study(train: Series, test: Series, measure: str = "R2", min_win: int = 1, max_win: int = 800, delta_win: int = 25):
    # Since our regressor depends on one parameter - the window size, we need to study it, in order to find the best forecaster for our data. For that, we implement the function rolling_mean_study as follows.
    # win_size = (3, 5, 10, 15, 20, 25, 30, 40, 50)
    win_size = [min_win] + [i*delta_win for i in range(1, int(max_win/delta_win)+1)]
    flag = measure == "R2" or measure == "MAPE"
    best_model = None
    best_params: dict = {"name": "Rolling Mean", "metric": measure, "params": ()}
    best_performance: float = -100000
    
    yvalues = []
    for w in win_size:
        pred = RollingMeanRegressor(win=w)
        pred.fit(train)
        prd_tst = pred.predict(test)
        
        eval: float = FORECAST_MEASURES[measure](test, prd_tst) #from dslabs_functions import FORECAST_MEASURES, DELTA_IMPROVE
        #print(w, eval)
        if eval > best_performance and abs(eval - best_performance) > DELTA_IMPROVE:
            best_performance: float = eval
            best_params["params"] = (w,)
            best_model = pred
        yvalues.append(eval)
    
    print(f"Rolling Mean best with win={best_params['params'][0]:.0f} -> {measure}={best_performance}")
    plot_line_chart(win_size, yvalues, title=f"Rolling Mean ({measure})", xlabel="window size", ylabel=measure, percentage=flag)
    #savefig(f"images/{file_tag}_rollingmean_{measure}_study.png")
    return best_model, best_params






target = "meter_reading"
train, test = series_train_test_split(data_ashrae[target], train_pct=0.90)


# 1. Simple Average
fr_mod = SimpleAvgRegressor(); fr_mod.fit(train); prd_trn: Series = fr_mod.predict(train); prd_tst: Series = fr_mod.predict(test)
plot_forecasting_eval(train, test, prd_trn, prd_tst, title=f"{file_tag} - Simple Average") #and now, we can see how the Simple Average model behaves over some real data.
plot_forecasting_series(train, test, prd_tst, title=f"{file_tag} - Simple Average", xlabel="timestamp", ylabel="meter_reading") #and now its visualization...

# 2. Persistence Model
fr_mod = PersistenceOptimistRegressor(); fr_mod.fit(train); prd_trn: Series = fr_mod.predict(train); prd_tst: Series = fr_mod.predict(test)
plot_forecasting_eval(train, test, prd_trn, prd_tst, title=f"{file_tag} - Persistence Optimist")
plot_forecasting_series(train, test, prd_tst, title=f"{file_tag} - Persistence Optimist", xlabel="timestamp", ylabel="meter_reading")

#PersistenceRealistRegressor
fr_mod = PersistenceRealistRegressor(); fr_mod.fit(train); prd_trn: Series = fr_mod.predict(train); prd_tst: Series = fr_mod.predict(test)
plot_forecasting_eval(train, test, prd_trn, prd_tst, title=f"{file_tag} - Persistence Realist")
plot_forecasting_series(train, test, prd_tst, title=f"{file_tag} - Persistence Realist", xlabel="timestamp", ylabel="meter_reading")


# 3. Exponential Smoothing
best_model, best_params = exponential_smoothing_study(train, test, measure=measure) # which when applied to our dataset finds the best model for the specific case, plotting the performace for each set of parameters:
params = best_params["params"]; prd_trn = best_model.predict(start=0, end=len(train) - 1); prd_tst = best_model.forecast(steps=len(test)) # And now we can see the best model and its performance.
plot_forecasting_eval(train, test, prd_trn, prd_tst, title=f"{file_tag} - Exponential Smoothing alpha={params[0]}") 
plot_forecasting_series(train, test, prd_tst, title=f"{file_tag} - Exponential Smoothing ", xlabel="timestamp", ylabel="meter_reading") #and its visualization...


# 4. Rolling Mean
fr_mod = RollingMeanRegressor(win=200); fr_mod.fit(train); prd_trn: Series = fr_mod.predict(train); prd_tst: Series = fr_mod.predict(test)
plot_forecasting_eval(train, test, prd_trn, prd_tst, title=f"{file_tag} - Rolling Mean")
plot_forecasting_series(train, test, prd_tst, title=f"{file_tag} - Rolling Mean", xlabel="timestamp", ylabel="meter_reading")
#rolling_mean_study
best_model, best_params = rolling_mean_study(train, test) # Now applied to our data #measure: str = "R2"
params = best_params["params"]; prd_trn: Series = best_model.predict(train); prd_tst: Series = best_model.predict(test) # And now, we may visualize the results achieved with the best parametrization:
plot_forecasting_eval(train, test, prd_trn, prd_tst, title=f"{file_tag} - Rolling Mean (win={params[0]})") 
plot_forecasting_series(train, test, prd_tst, title=f"{file_tag} - Rolling Mean (win={params[0]})", xlabel="timestamp", ylabel="meter_reading") 


# 5. Linear Regression
# Linear Regression models just assume that the time series follows a linear trend, and looks for the line that minimizes the sum of square errors. In order to implement it we just need to use the Linear Regressor sklearn class.
trnX = arange(len(train)).reshape(-1, 1); tstX = arange(len(train), len(train)+len(test)).reshape(-1, 1); trnY = train.to_numpy(); tstY = test.to_numpy()
model = LinearRegression(); model.fit(trnX, trnY) #from sklearn.linear_model import LinearRegression
prd_trn: Series = Series(model.predict(trnX), index=train.index); prd_tst: Series = Series(model.predict(tstX), index=test.index)
plot_forecasting_eval(train, test, prd_trn, prd_tst, title=f"{file_tag} - Linear Regression") 
plot_forecasting_series(train, test, prd_tst, title=f"{file_tag} - Linear Regression", xlabel="timestamp", ylabel="meter_reading") 






# 6. ARIMA
#ARIMA receives three mandatory parameters p, d, q, but it works a little different from the other estimators we have been using from sklearn, since it is implemented in the statsmodels.tsa package.
#Like before we create the ARIMA object, but now we pass the data to model and the parameters to use. After this we fit the model, which is returned as a ARIMAResults object.
filename: str = "data/time_series/ashrae.csv"; file_tag: str = "ASHRAE"; target: str = "meter_reading"; timecol: str = "timestamp"; measure: str = "R2"
data: DataFrame = read_csv(filename, index_col=timecol, sep=",", decimal=".", parse_dates=True)
series: Series = data[target]
train, test = series_train_test_split(data, trn_pct=0.90) #from dslabs_functions import series_train_test_split, HEIGHT

predictor = ARIMA(train, order=(3, 1, 2)); model = predictor.fit() #from statsmodels.tsa.arima.model import ARIMA
print(model.summary())

#These results can be summarized and plotted in a fashionable way through the plot_diagnostics method, which shows the following plots (ordered clockwise from top left):
#Standardized residuals over time. #Histogram plus estimated density of standardized residuals, along with a Normal(0,1) density plotted for reference. #Normal Q-Q plot, with Normal reference line. #Correlogram
model.plot_diagnostics(figsize=(2 * HEIGHT, 1.5 * HEIGHT))

#So, as usual, in order to find the best model, we need to look for the best (p, d, q) parameters...
def arima_study(train: Series, test: Series, measure: str = "R2"):
    d_values = (0, 1, 2)
    p_params = (1, 2, 3, 5, 7, 10)
    q_params = (1, 3, 5, 7)
    
    flag = measure == "R2" or measure == "MAPE"
    best_model = None
    best_params: dict = {"name": "ARIMA", "metric": measure, "params": ()}
    best_performance: float = -100000
    
    fig, axs = subplots(1, len(d_values), figsize=(len(d_values) * HEIGHT, HEIGHT))
    for i in range(len(d_values)):
        d: int = d_values[i]
        values = {}
        for q in q_params:
            yvalues = []
            for p in p_params:
                arima = ARIMA(train, order=(p, d, q))
                model = arima.fit()
                prd_tst = model.forecast(steps=len(test), signal_only=False)
                eval: float = FORECAST_MEASURES[measure](test, prd_tst) #from dslabs_functions import FORECAST_MEASURES, DELTA_IMPROVE
                # print(f"ARIMA ({p}, {d}, {q})", eval)
                if eval > best_performance and abs(eval - best_performance) > DELTA_IMPROVE:
                    best_performance: float = eval
                    best_params["params"] = (p, d, q)
                    best_model = model
                yvalues.append(eval)
            values[q] = yvalues
        plot_multiline_chart(p_params, values, ax=axs[i], title=f"ARIMA d={d} ({measure})", xlabel="p", ylabel=measure, percentage=flag)
    print(f"ARIMA best results achieved with (p,d,q)=({best_params['params'][0]:.0f}, {best_params['params'][1]:.0f}, {best_params['params'][2]:.0f}) ==> measure={best_performance:.2f}")
    
    return best_model, best_params

#which when applied to our dataset finds the best model for the specific case, plotting the performace for each set of parameters:
best_model, best_params = arima_study(train, test, measure=measure) #savefig(f"images/{file_tag}_arima_{measure}_study.png")

#And now we can see the best model and its performance.
params = best_params["params"]
prd_trn = best_model.predict(start=0, end=len(train) - 1)
prd_tst = best_model.forecast(steps=len(test))

plot_forecasting_eval(train, test, prd_trn, prd_tst, title=f"{file_tag} - ARIMA (p={params[0]}, d={params[1]}, q={params[2]})") #savefig(f"images/{file_tag}_arima_{measure}_eval.png")
#and its visualization...
plot_forecasting_series(train, test, prd_tst, title=f"{file_tag} - ARIMA ", xlabel=timecol, ylabel=target) #savefig(f"images/{file_tag}_arima_{measure}_forecast.png")














# 7. LSTMs
#There are two major implementations of LSTMs, and we are using the one available through torch package.
#In order to simplify the task, lets define a class DS_LSTM to encapsulate our implementation, after defining a small function to transform our series into tensor data structures - the prepare_dataset_for_lstm function.
def prepare_dataset_for_lstm(series, seq_length: int = 4):
    setX: list = []
    setY: list = []
    for i in range(len(series) - seq_length):
        past = series[i : i + seq_length]
        future = series[i + 1 : i + seq_length + 1]
        setX.append(past)
        setY.append(future)
    return tensor(setX), tensor(setY)

class DS_LSTM(Module):
    def __init__(self, train, input_size: int = 1, hidden_size: int = 50, num_layers: int = 1, length: int = 4):
        super().__init__()
        self.lstm = LSTM(input_size=input_size, hidden_size=hidden_size, num_layers=num_layers, batch_first=True)
        self.linear = Linear(hidden_size, 1)
        self.optimizer = Adam(self.parameters())
        self.loss_fn = MSELoss()
        
        trnX, trnY = prepare_dataset_for_lstm(train, seq_length=length)
        self.loader = DataLoader(TensorDataset(trnX, trnY), shuffle=True, batch_size=len(train) // 10)
    
    def forward(self, x):
        x, _ = self.lstm(x)
        x = self.linear(x)
        return x
    
    def fit(self):
        self.train()
        for batchX, batchY in self.loader:
            y_pred = self(batchX)
            loss = self.loss_fn(y_pred, batchY)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()
        return loss
    
    def predict(self, X):
        with no_grad():
            y_pred = self(X)
        return y_pred[:, -1, :]

#In order to simplify the task, some parameters are fixed, such as the optimizer and loss function, Adam and MSE respectively. Beside that, we are able to choose the parameters depending on the data:
#input_size: to define the number of variables describing the data;
#hidden_size: to define the number of hidden units inside each LSTM cell (do not mistake with the number of states in the LSTM);
#num_layers: to define the number of layers of LSTM cells (do not mistake with the number of states in the LSTM).

filename: str = "data/time_series/ashrae.csv"; file_tag: str = "ASHRAE"; target: str = "meter_reading"; timecol: str = "timestamp"; measure: str = "R2"
data: DataFrame = read_csv(filename, index_col=timecol, sep=",", decimal=".", parse_dates=True)
series = data[[target]].values.astype("float32")
train_size = int(len(series) * 0.90)
train, test = series[:train_size], series[train_size:]

#Now that we have the train and test dataframes, we need to transform them into sets of smaller sequences, preferably, with a fixed length (specified through seq_length parameter). Beside that, we need to convert the data to a Tensor format.
#After this, is then possible to create our LSTM and training it through the fit method.
model = DS_LSTM(train, input_size=1, hidden_size=50, num_layers=1); loss = model.fit()
print(loss)


def lstm_study(train, test, nr_episodes: int = 1000, measure: str = "R2"):
    sequence_size = [2, 4, 8]
    nr_hidden_units = [25, 50, 100]
    
    step: int = nr_episodes // 10
    episodes = [1] + list(range(0, nr_episodes + 1, step))[1:]
    flag = measure == "R2" or measure == "MAPE"
    best_model = None
    best_params: dict = {"name": "LSTM", "metric": measure, "params": ()}
    best_performance: float = -100000
    
    _, axs = subplots(1, len(sequence_size), figsize=(len(sequence_size) * HEIGHT, HEIGHT))
    
    for i in range(len(sequence_size)):
        length = sequence_size[i]
        tstX, tstY = prepare_dataset_for_lstm(test, seq_length=length)
        
        values = {}
        for hidden in nr_hidden_units:
            yvalues = []
            model = DS_LSTM(train, hidden_size=hidden)
            for n in range(0, nr_episodes + 1):
                model.fit()
                if n % step == 0:
                    prd_tst = model.predict(tstX)
                    eval: float = FORECAST_MEASURES[measure](test[length:], prd_tst) #from dslabs_functions import FORECAST_MEASURES, DELTA_IMPROVE
                    print(f"seq length={length} hidden_units={hidden} nr_episodes={n}", eval)
                    if eval > best_performance and abs(eval - best_performance) > DELTA_IMPROVE:
                        best_performance: float = eval
                        best_params["params"] = (length, hidden, n)
                        best_model = deepcopy(model) #from copy import deepcopy
                    yvalues.append(eval)
            values[hidden] = yvalues
        plot_multiline_chart(episodes, values, ax=axs[i], title=f"LSTM seq length={length} ({measure})", xlabel="nr episodes", ylabel=measure, percentage=flag)
    print(f"LSTM best results achieved with length={best_params["params"][0]} hidden_units={best_params["params"][1]} and nr_episodes={best_params["params"][2]}) ==> measure={best_performance:.2f}")
    return best_model, best_params
best_model, best_params = lstm_study(train, test, nr_episodes=3000, measure=measure)

#To assess the results, we just need to use the model to predict the target variable, and measure the usual metrics like the R2. We may do it both on the training and test datasets.
params = best_params["params"]
best_length = params[0]
trnX, trnY = prepare_dataset_for_lstm(train, seq_length=best_length)
tstX, tstY = prepare_dataset_for_lstm(test, seq_length=best_length)

prd_trn = best_model.predict(trnX); prd_tst = best_model.predict(tstX)

plot_forecasting_eval(train[best_length:], test[best_length:], prd_trn, prd_tst, title=f"{file_tag} - LSTM (length={best_length}, hidden={params[1]}, epochs={params[2]})") #savefig(f"images/{file_tag}_lstms_{measure}_eval.png")

#Now, we are able to study the impact of the different parameters on the LSTM results.
series = data[[target]]
train, test = series[:train_size], series[train_size:]
pred_series: Series = Series(prd_tst.numpy().ravel(), index=test.index[best_length:])

plot_forecasting_series(train[best_length:], test[best_length:], pred_series, title=f"{file_tag} - LSTMs ", xlabel=timecol, ylabel=target) #savefig(f"images/{file_tag}_lstms_{measure}_forecast.png")





