import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.api import VAR
from scipy.stats import pearsonr
import python_scripts.data_handling.data_handler as dd


# https://github.com/ritvikmath/Time-Series-Analysis/blob/master/VAR%20Model.ipynb
# load data
user_data = dd.load_and_prep_for_var()

index = 2 # for now chose second column (temp)

# # column_series
# Select all columns except the last one and convert them to float

column_series = user_data.asfreq(pd.infer_freq(user_data.index))

# # 1 normalise data

avgs= column_series.mean()
devs = column_series.std()

#column_series = (column_series-avg)/ dev
for col in column_series.columns:
    column_series[col] = (column_series[col] - avgs.loc[col]) / devs.loc[col]

spalte1 = 'DSP_FLOOR_DISTRIBUTOR_RUECKLAUFTEMPERATUR_EQUIPMENT_ID_Value'
spalte2 = 'DSP_FLOOR_DISTRIBUTOR_VORLAUFTEMPERATUR_EQUIPMENT_ID_Value'
# 2 remove stationarity

column_series = column_series.diff().dropna() # first value doesn't have predecessor



# # 3 remove volatility

annual_volatility = column_series.groupby(column_series.index.year).std()

column_annual_volatility = column_series.index.map(lambda d: annual_volatility.loc[d.year])
column_series[spalte1+'_anual_vol'] = column_series.index.map(lambda d: annual_volatility.loc[d.year, spalte1])
column_series[spalte2+'_anual_vol'] = column_series.index.map(lambda d: annual_volatility.loc[d.year, spalte2])

column_series[spalte1] = column_series[spalte1] / column_series[spalte1+'_anual_vol']
column_series[spalte2] = column_series[spalte2] / column_series[spalte2+'_anual_vol']

# 4 remove seasonability

# Calculate monthly averages for spalte1 and spalte2
month_avgs_spalte1 = column_series.groupby(column_series.index.month)[spalte1].mean()
month_avgs_spalte2 = column_series.groupby(column_series.index.month)[spalte2].mean()

# Subtract the monthly average for spalte1 and spalte2
column_series[spalte1] = column_series[spalte1] - column_series.index.map(lambda d: month_avgs_spalte1.loc[d.month])
column_series[spalte2] = column_series[spalte2] - column_series.index.map(lambda d: month_avgs_spalte2.loc[d.month])


# PACF partial  Autocorrelation Function (PACF):

# plot_pacf(column_series[spalte1])
# plt.show()


# correlation between spalte1 and spalte2

for lag in range(1, 25):
    series1 = column_series[spalte1].iloc[lag:]
    series2 = column_series[spalte2].iloc[:-lag]
    print('Lag: %s'%lag)
    print(pearsonr(series1, series2))
    print('------')




    # # plot nur ruecklauf
# plt.figure(figsize=(12,6))
# ruecklauf_temp = plt.plot(column_series[spalte1])

# for year in range(2021, 2023):
#     plt.axvline(datetime(year,1,1), linestyle='--', color='k', alpha=0.3)

# plt.axhline(0, linestyle='--', color='k', alpha=0.3)
# plt.ylabel('First Difference', fontsize=18)
# plt.legend(['Ruecklauftemp'], fontsize=16)
# plt.show()

# #plot beide
# plt.figure(figsize=(12,6))
# ruecklauf_temp = plt.plot(column_series['DSP_FLOOR_DISTRIBUTOR_RUECKLAUFTEMPERATUR_EQUIPMENT_ID_Value'])
# vorlauf_temp = plt.plot(column_series['DSP_FLOOR_DISTRIBUTOR_VORLAUFTEMPERATUR_EQUIPMENT_ID_Value'], color='red')

# for year in range(2021, 2023):
#     plt.axvline(datetime(year,1,1), linestyle='--', color='k', alpha=0.5)

# plt.legend(['Ruecklauftemp', 'Vorlauftemp'], fontsize=16)
# plt.show()
    


    # month_avgs = column_series.groupby(column_series.index.month).mean() # averages per month
# column_series[spalte1 + '_month_avg'] = column_series.index.map(lambda d: month_avgs.loc[d.month, spalte1])
# column_series[spalte2 + '_month_avg'] = column_series.index.map(lambda d: month_avgs.loc[d.month, spalte2])

# column_series[spalte1] = column_series[spalte1]- column_series[spalte1+ '_month_avg']
# column_series[spalte2]  = column_series[spalte2] - column_series[spalte2+ '_month_avg']

# data_month_avg = column_series.index.map(lambda d: month_avgs.loc[d.month])
# column_series = column_series - data_month_avg