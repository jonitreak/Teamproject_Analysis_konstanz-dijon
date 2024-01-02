import pandas as pd
import numpy as np
import os as os


#maybe needs different datatype
def loaData(): 
    """
    Prompt the user for a CSV file path, load it into a pandas DataFrame,
    and allow the user to retry if the path is incorrect or exit by entering '0'.
    """
    while True:
        # Prompt the user to enter the file path
        path = input("Please enter the path to the CSV file or '0' to exit: ")

        # Check if the user wants to exit
        if path == '0':
            print("Exiting the program.")
            return None

        # Normalize the file path for the current operating system to ensure crossplattform compabilty
        normalized_path = os.path.normpath(path)

        try:
            # Load the CSV file into a DataFrame
            dataframe = pd.read_csv(normalized_path)
            return dataframe
        except Exception as e:
            print(f"An error occurred: {e}. Please try again.")


def get_column_names(dataframe):
    return dataframe.columns.tolist()

def get_time_series(dataframe, column_name):
    time_series = np.array(dataframe[column_name])
    return time_series

#maybe needs different datatype
def sliceDataByTime(dataframe: np.array):
    #TODO Implement
    pass
