# Teamproject/ Sensor Data Analysis

A binational project of the university of applied science Konstanz, Germany and the institut of technology Esirem, Dijon.
Contributing students: 

- Mirjam Abele (Konstanz)
- Joachim Druhet (Dijon)
- Mahaut Galice (Dijon)
- Viktoria Stiem (Konstanz)
- Aida Vehapi (Konstanz)
- Elida Vehapi (Konstanz)

## Table of Contents
- [Teamproject/ Sensor Data Analysis](#teamproject-sensor-data-analysis)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
    - [Data Sources](#data-sources)
      - [BOSCH](#bosch)
  - [Code Usage Documentation](#code-usage-documentation)
    - [start](#start)
      - [Classes and Methods](#classes-and-methods)
        - [`Start` Class](#start-class)
          - [Methods](#methods)
          - [`__init__(self)`](#__init__self)
          - [`run_client(self, client_name)`](#run_clientself-client_name)
          - [`get_user_input(self)`](#get_user_inputself)
          - [`start(self)`](#startself)
        - [Data Handling](#data-handling)
          - [`parser(date: str)`](#parserdate-str)
          - [`loaData()`](#loadata)
          - [`load_and_prep_for_var()`](#load_and_prep_for_var)
          - [`get_column_names(dataframe)`](#get_column_namesdataframe)
          - [`get_time_series(dataframe, column_name)`](#get_time_seriesdataframe-column_name)
          - [`get_valid_date(prompt)`](#get_valid_dateprompt)
        - [Fourier Handler](#fourier-handler)
          - [`main()`](#main)
        - [Fourier Calculation](#fourier-calculation)
          - [`smooth_signal(data, window_size)`](#smooth_signaldata-window_size)
          - [`perform_fourier_analysis(data, column_name, start_date, end_date, smoothing_window_size=3)`](#perform_fourier_analysisdata-column_name-start_date-end_date-smoothing_window_size3)
          - [`filter_frequencies(freqs, fft_result)`](#filter_frequenciesfreqs-fft_result)
          - [`inverse_fourier(filtered_freqs, filtered_fft_result, original_length)`](#inverse_fourierfiltered_freqs-filtered_fft_result-original_length)
          - [`identify_anomalies(original_data, reconstructed_data, threshold_multiplier=1)`](#identify_anomaliesoriginal_data-reconstructed_data-threshold_multiplier1)
          - [`visualize_reconstructed_data(ax, timestamps, original_data, reconstructed_data, anomalies, threshold)`](#visualize_reconstructed_dataax-timestamps-original_data-reconstructed_data-anomalies-threshold)
          - [`do_fourier(data, column_name, start_date, end_date)`](#do_fourierdata-column_name-start_date-end_date)


## Introduction

The project aims to provide a sustainable programm to analyse dataframes. 


### Data Sources
#### BOSCH
- DSP= Deckenstrahlplatte (heating on the ceiling)
- ERRECHNETE_RAUMTEMPERATURE_DSP = set temperature for this heating
- RBG_RAUMTEMPERATUR = temperature of the room
- ANSTEUERUNG_DSP_VENTIL = valve control for DSP heating
- DSP_FLOOR_DISTRIBUTOR_DURCHFLUSS = volume flow at floor distributor to DSP heating [m^3/h]
- DSP_FLOOR_DISTRIBUTOR_RUECKLAUFTEMPERATUR = temperature of outcoming volume flow [°C]
- DSP_FLOOR_DISTRIBUTOR_VORLAUFTEMPERATUR = temperature of incoming volume flow [°C]
- DSP_FLOOR_DISTRIBUTOR_LEISTUNG_EQUIPMENT = power of heating [kW]
- HK_CIRCUIT = heating circuit (hot circuit)
- KK_CIRCUIT = cooling circuit (cold circuit)
- VL = incoming volume flow
- RL = outcoming volume flow


## Code Usage Documentation

### start
The `start.py` script is designed to allow the user to run different Python clients based on their selection. For now only a fourier client has been implemented but the architecture provides the structure to easily add on further clients.


1. **Run the Script**: Execute the `start.py` script using a Python interpreter. This should be done from the root directory.

    ```bash
    python start.py
    ```

2. **Enter Client Name**: When prompted, enter the name of the client you want to run. The available clients are "fourier".

3. **Execution**: The script will run the selected client script using the respective module.



#### Classes and Methods

##### `Start` Class

This class is the entry point of the application.

###### Methods

###### `__init__(self)`
- Initializes the `Start` class instance.
- Sets `available_clients`, a list of client names that can be run (currently only "fourier").

###### `run_client(self, client_name)`
- Runs a specific client based on user input.
- Parameters:
  - `client_name` (str): The name of the client to run.
- Currently supports:
  - Running "fourier" client using dynamic import with `importlib`.

###### `get_user_input(self)`
- Prompts the user to select a client from the available options.
- Returns the name of the selected client.

###### `start(self)`
- Starts the program.
- Gets user input for client selection and runs the selected client.

##### Data Handling 

###### `parser(date: str)`
- Parses a datetime string in a specific format.
- Parameters:
  - `date` (str): Datetime string to parse.
- Returns a `datetime` object.

###### `loaData()`

- Reads data from a CSV file and returns it as a pandas DataFrame.

###### `load_and_prep_for_var()`
- Loads and prepares data for VAR (Vector Autoregression) analysis.
- Normalizes file paths, reads CSV data, and processes it for VAR analysis.
- Returns a pandas DataFrame.

###### `get_column_names(dataframe)`
- Retrieves column names from a pandas DataFrame.
- Parameters:
  - `dataframe`: The DataFrame to process.
- Returns a list of column names.

###### `get_time_series(dataframe, column_name)`
- Extracts a time series from a DataFrame based on the specified column name.
- Parameters:
  - `dataframe`: The DataFrame to process.
  - `column_name` (str): Name of the column to extract the time series from.
- Returns a numpy array of the time series.

###### `get_valid_date(prompt)`
- Prompts the user to enter a date and validates its format.
- Repeatedly prompts the user until a valid date in the format 'YYYY-MM-DD' is entered.
- Parameters:
  - `prompt` (str): The prompt message to display.
- Returns the validated date string.

##### Fourier Handler

This module contains the main function for handling user inputs for Fourier analysis.

###### `main()`
- Entry point for the Fourier client.
- Loads data, prompts the user for column selection, and performs Fourier analysis based on the selected column and date range.
- Utilizes functions from `data_handling` and `fourier` modules.

##### Fourier Calculation 

This module contains functions for performing and visualizing Fourier analysis.

###### `smooth_signal(data, window_size)`
- Smoothens the signal using a rolling window average.
- Parameters:
  - `data`: The data to smooth.
  - `window_size` (int): The size of the smoothing window.

###### `perform_fourier_analysis(data, column_name, start_date, end_date, smoothing_window_size=3)`
- Performs Fourier analysis on the specified data column within the given date range.
- Parameters:
  - `data`: The DataFrame containing the data.
  - `column_name` (str): The column to analyze.
  - `start_date`, `end_date` (str): The start and end dates for the analysis.
  - `smoothing_window_size` (int): The size of the smoothing window.
- Returns frequencies, Fourier transform results, timestamps, and smoothed column values.

###### `filter_frequencies(freqs, fft_result)`
- Filters frequencies based on an amplitude threshold.
- Parameters:
  - `freqs`: The frequencies to filter.
  - `fft_result`: The Fourier transform result.
- Returns filtered frequencies and Fourier transform results.

###### `inverse_fourier(filtered_freqs, filtered_fft_result, original_length)`
- Performs inverse Fourier transformation to reconstruct the original signal.
- Parameters:
  - `filtered_freqs`: The filtered frequencies.
  - `filtered_fft_result`: The filtered Fourier transform result.
  - `original_length` (int): The length of the original signal.
- Returns the reconstructed signal.

###### `identify_anomalies(original_data, reconstructed_data, threshold_multiplier=1)`
- Identifies anomalies in the reconstructed signal compared to the original data.
- Parameters:
  - `original_data`, `reconstructed_data`: The original and reconstructed data.
  - `threshold_multiplier` (float): Multiplier for the threshold.
- Returns identified anomalies and the threshold.

###### `visualize_reconstructed_data(ax, timestamps, original_data, reconstructed_data, anomalies, threshold)`
- Visualizes the original and reconstructed data, highlighting anomalies.
- Parameters:
  - `ax`: The matplotlib axis to plot on.
  - `timestamps`: The timestamps for the data.
  - `original_data`, `reconstructed_data`: The original and reconstructed data.
  - `anomalies`: Boolean array indicating anomalies.
  - `threshold`: The threshold for identifying anomalies.

###### `do_fourier(data, column_name, start_date, end_date)`
- Main function to execute the Fourier analysis process.
- Parameters:
  - `data`: The DataFrame containing the data.
  - `column_name` (str): The column to analyze.
  - `start_date`, `end_date` (str): The start and end dates for the analysis.
- Visualizes the Fourier analysis results.
