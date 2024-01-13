import pandas as pd
import numpy as np
import os as os
from datetime import datetime


def parser(date: str):
    # '2021-01-26T10:00:00.0000000Z' -> '2021-01-26T10:00:00.000000'
    truncated_datetime_string = date[:-2]

    # Parse the truncated string with datetime.strptime
    return datetime.strptime(truncated_datetime_string, '%Y-%m-%dT%H:%M:%S.%f')


# load data for fourier
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

def load_and_prep_for_var():
    # Loop for file path input
    while True:
        #path = input("Please enter the path to the CSV file or '666' to exit: ")
        #path = "C:\\Users\\Viktoria Stiem\\Documents\\htwg Konstanz\\2324Wise\\teamprojekt\\code\\Teamproject_Analysis\\src\\data\\Daten_pandas_2_weeks.csv"
        path = "C:\\Users\\Viktoria Stiem\\Documents\\htwg Konstanz\\2324Wise\\teamprojekt\\code\\Teamproject_Analysis\\src\\data\\daten.csv"
        if path == '666':
            print("Exiting the program.")
            print("1")
            return None
        else:
            # Normalize the file path for cross-platform compatibility
            normalized_path = os.path.normpath(path)
            break

    # Loop for column index input
    # while True:
    #     index = input("Please enter the column index of the date/timestamp or '666' to exit: ")
    #     if index == '666':
    #         print("2")
    #         print("Exiting the program.")
    #         return None
    #     try:
    #         # Attempt to convert the index to an integer
    #         index = int(index)-1
    #         break
    #     except ValueError:
    #         print("Invalid input for column index. Please enter a valid integer.")
    index = 14
    try:
        dataframe = pd.read_csv(normalized_path, parse_dates=[index], index_col=index, date_parser=parser)

        # Replace commas with dots and convert columns to float
        for col in dataframe.columns[:-1]:  # Exclude the last column
            dataframe[col] = dataframe[col].astype(str).str.replace(',', '.').astype(float)

        dataframe = dataframe.resample('H').mean()
        return dataframe
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
        return None

def get_column_names(dataframe):
    return dataframe.columns.tolist()

def get_time_series(dataframe, column_name):
    time_series = np.array(dataframe[column_name])
    return time_series


