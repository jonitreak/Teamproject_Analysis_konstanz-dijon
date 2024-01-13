import pandas as pd
import numpy as np
import os as os
from datetime import datetime


def parser(date: str):
    return datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%fZ')


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
        path = input("Please enter the path to the CSV file or '666' to exit: ")
        if path == '666':
            print("Exiting the program.")
            return None
        else:
            # Normalize the file path for cross-platform compatibility
            normalized_path = os.path.normpath(path)
            break

    # Loop for column index input
    while True:
        index = input("Please enter the column index of the date/timestamp or '666' to exit: ")
        if index == '666':
            print("Exiting the program.")
            return None
        try:
            # Attempt to convert the index to an integer
            index = int(index)
            break
        except ValueError:
            print("Invalid input for column index. Please enter a valid integer.")

    try:
        # Load the CSV file into a DataFrame and parse the specified column as dates
        dataframe = pd.read_csv(normalized_path, parse_dates=[index], index_col=index, date_parser=parser) # maybe needs squeeze=True param
        return dataframe
    except Exception as e:
        print(f"An error occurred: {e}. Please try again.")
        return None

def get_column_names(dataframe):
    return dataframe.columns.tolist()

def get_time_series(dataframe, column_name):
    time_series = np.array(dataframe[column_name])
    return time_series


