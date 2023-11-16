import pandas as pd
import numpy as np
import fourier as f
import matplotlib.pyplot as plt

# Daten aus der CSV-Datei laden
dataframe = pd.read_csv("your\path")
column_name = 'RM_RBG_RAUMTEMPERATUR_POINT_ID_Value'
time_series = np.array(dataframe[column_name])

window_size = 5         # 4 - 8
smoothed_series = f.smooth_signal(time_series, window_size)

# # intervall
intervall = 15*60.0
f.fourierPlot(smoothed_series, intervall)

# plt.plot( smoothed_series)
# plt.show()
