# DATASETS # Colocar outros Datasets disponíveis (WMM [Lab2, Projeto], etc.)
from pandas import read_csv, Series, DataFrame, concat, Index, Period


# CLASSIFICATION
data_ny_arrests: DataFrame = read_csv('data/class_ny_arrests.csv', index_col="ARREST_DATE", na_values="", parse_dates=True, dayfirst=True); data_ny_arrests.sort_index(inplace=True) #target = "ny_arrests" #file_tag = "class_ny_arrests"
data_cancer: DataFrame = read_csv("data/stroke.csv", index_col="id", na_values=""); data_cancer.sort_index(inplace=True) #target = "stroke" #file_tag = "stroke"
data_fin_distress: DataFrame = read_csv('data/class_financial distress.csv', na_values="") #target = "financial distress" #file_tag = "class_financial distress"
data_gdindex: DataFrame = read_csv("data/gdindex.csv", index_col="ISO3") #file_tag = "gdindex" # Não está no formato Time series


# TIME SERIES
data_algae: DataFrame = read_csv("data/algae.csv", index_col="date", na_values="", parse_dates=True, infer_datetime_format=True, dayfirst=False) #file_tag = "algae" #data_algae["date"] = to_datetime(data_algae["date"], format='%d/%m/%Y') #data_algae.set_index("date", inplace=True) #data_algae["date"] = data_algae.index 
data_portugal_population: DataFrame = read_csv("data/time_series/portugal_population.csv", index_col="date", sep=",", decimal=".", parse_dates=True, infer_datetime_format=True) #file_tag = "portugal_population" #target = "LifeExpectancy" #target = "Population"
data_gdp_europe: DataFrame = read_csv('data/time_series/forecast_gdp_europe.csv', index_col="Year", na_values="", parse_dates=True, infer_datetime_format=True, dayfirst=True) #file_tag = "forecast_gdp_europe" #target = "gdp_europe"
data_psngr: DataFrame = read_csv("data/time_series/airline_passengers.csv", index_col="Month", na_values="", parse_dates=True, dayfirst=True) #file_tag = "airline_passengers" 
data_ashrae: DataFrame = read_csv("data/time_series/ashrae.csv", index_col="timestamp", sep=",", decimal=".", parse_dates=True, infer_datetime_format=True) #target = "meter_reading" #file_tag = "ashrae"
data_appliances: DataFrame = read_csv('data/time_series/appliances.csv', index_col="date", sep=",", decimal=".", na_values="", parse_dates=True, dayfirst=True, infer_datetime_format=True) #target = "Appliances" #file_tag = "appliances" # Este dataset tem horas na coluna "date"
#psngr: Series = Series(data=data_psngr['Passengers'], index=data_psngr.index, name='passengers')
#ashrae: Series = Series(data=data_ashrae["meter_reading"], index=data_ashrae.index, name='ashrae')
data_price: DataFrame = read_csv("data/time_series/stock_price.csv", index_col="Date", sep=",", decimal=".") #target = "Price" #file_tag = "stock_price"


# ECONOMETRIA #pd.read_stata("C:/Users/João Paulo/Desktop/IST/ECO/Proj/Project/affairs.dta")
data_auto: DataFrame = read_csv("data/auto.csv", na_values="")
data_labour_force: DataFrame = read_csv("data/labour_force.csv", na_values="")
data_ceo_salary: DataFrame = read_csv("data/ceo_salary.csv", na_values="")
data_sex_workers: DataFrame = read_csv("data/sex_workers.csv", na_values="") 
data_card_week5: DataFrame = read_csv("data/card_week5.csv", index_col="id", na_values="")
data_affairs: DataFrame = read_csv("data/affairs.csv", index_col="id", na_values="")




