import pandas as pd
import numpy as np
import os as os

#maybe needs different datatype
def loaData(path): 

    dataframe = pd.read_csv(path)
    return dataframe


# def validade_path(path):
#     #TODO FIX !!
#     if path.find("\"") != -1:
#         path = path.replace("\"", "")
#     if path.find("\\") != -1:
#         path = path.replace("\\", "\\\\")

#     _, file_extension = os.path.splitext(path.lower())
#     return file_extension == ".csv"

def get_column_names(dataframe):
    return dataframe.columns.tolist()

def get_time_series(dataframe, column_name):
    time_series = np.array(dataframe[column_name])
    return time_series

#maybe needs different datatype
def sliceDataByTime(dataframe: np.array):
    #TODO Implement
    pass
