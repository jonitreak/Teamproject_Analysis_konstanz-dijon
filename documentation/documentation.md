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
  - [Project Overview](#project-overview)
  - [Data Collection](#data-collection)
    - [Data Sources](#data-sources)
      - [BOSCH](#bosch)
    - [Data Preparation](#data-preparation)
  - [Data Analysis](#data-analysis)
    - [Fourier Data Analysis](#fourier-data-analysis)
    - [OTHER Analysis](#other-analysis)
  - [Results](#results)
  - [Visualization](#visualization)
  - [Code Usage Documentation](#code-usage-documentation)
    - [start](#start)
      - [Classes and Methods](#classes-and-methods)
        - [`Start` Class](#start-class)
          - [`run_client(self, client_name)`](#run_clientself-client_name)
          - [`get_user_input(self)`](#get_user_inputself)
          - [`start(self)`](#startself)
        - [Example Usage](#example-usage)
    - [fourier\_client](#fourier_client)
      - [Usage](#usage)
      - [Notes](#notes)
    - [Data Module](#data-module)
      - [Functions](#functions)
        - [`loadData(path)`](#loaddatapath)
        - [`validate_path(path)`](#validate_pathpath)
        - [`get_column_names(dataframe)`](#get_column_namesdataframe)
        - [`get_time_series(dataframe, column_name)`](#get_time_seriesdataframe-column_name)
        - [`sliceDataByTime(dataframe: np.array)`](#slicedatabytimedataframe-nparray)
      - [Notes](#notes-1)
  - [Conclusion](#conclusion)
  - [Contributing](#contributing)
  - [License](#license)
  - [Acknowledgements](#acknowledgements)


## Introduction

Provide a brief introduction to the sensory data analysis project. Explain the context, objectives, and the significance of the project.

## Project Overview

Summarize the overall structure and goals of the project. Provide an outline of the tasks and components involved in the analysis.

## Data Collection

Explain how data was collected for the sensory analysis. Include details about the data sources and the steps taken to prepare the data for analysis.

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

<!-- List the sources from which sensory data was collected. Include any relevant information about the data collection process. -->

### Data Preparation

Describe the data cleaning and preprocessing steps, including data normalization, handling missing values, and any other necessary data transformations.

## Data Analysis

Explain the methods and techniques used for analyzing sensory data.

### Fourier Data Analysis



### OTHER Analysis

Discuss the statistical methods applied to the sensory data, such as hypothesis testing, ANOVA, or regression analysis.


## Results

Present the key results and findings of the sensory data analysis. Use tables, graphs, or any other relevant visualization tools to support your findings.

## Visualization

Include any visualizations, graphs, or charts that help illustrate the analysis and results.

## Code Usage Documentation

### start
The `start.py` script is designed to allow the user to run different Python clients based on their selection. The script prompts the user to enter the name of the client they want to run, and based on the input, it executes the corresponding client script using the `subprocess` module.


1. **Run the Script**: Execute the `start.py` script using a Python interpreter.

    ```bash
    python start.py
    ```

2. **Enter Client Name**: When prompted, enter the name of the client you want to run. The available clients are "fourier", "multiactor", and "data".

3. **Execution**: The script will run the selected client script using the `subprocess` module.



#### Classes and Methods

##### `Start` Class

###### `run_client(self, client_name)`

- Runs a specific client based on the user input.

    - **Parameters**:
        - `client_name` (str): The name of the client to run.

###### `get_user_input(self)`

- Gets user input for selecting a client.

    - **Returns**:
        - `str`: The name of the selected client.

###### `start(self)`

- Starts the program, gets user input, and runs the selected client.

##### Example Usage

```python
if __name__ == "__main__":
    start_instance = Start()
    start_instance.start()

```

### fourier_client
The Fourier Client script (`fourier_client.py`) is designed to perform Fourier analysis on a selected column of a CSV file. It uses functions from the `data` and `python_scripts.analysis.fourier` modules to load data, select a column, and generate a Fourier plot.

#### Usage

1. **Load File**: File is loaded using data module. TODO

2. **Column Selection**: The script prompts the user to select a column from the loaded CSV file for Fourier analysis.

3. **Window Size**: Specify the window size for smoothing the time series. Enter numeric characters when prompted.

4. **Interval**: The time interval between measurements is set to 15 minutes by default (hardcoded). TODO 

5. **Result**: The script generates a Fourier plot based on the selected column, window size, and time interval.

#### Notes
TODO
- The path to the CSV file is currently hardcoded as "your\path". Update the `file_path` variable for the actual path or implement dynamic user input (TODO: Code in comments needs to be fixed).

- The **windowsize** and time **interval** are currently hardcoded. You can customize them by updating the `window_size` and `intervall` variables.

- To exit the script at any prompt, enter "666".

---

### Data Module

The `data` module provides functions for loading and manipulating data from CSV files. It includes methods for loading a CSV file into a Pandas DataFrame, validating file paths, getting column names, and extracting time series data.

#### Functions

##### `loadData(path)`

- **Description**: Loads data from a CSV file into a Pandas DataFrame.

- **Parameters**:
  - `path` (str): The path to the CSV file.

- **Returns**:
  - `pd.DataFrame`: The loaded DataFrame.

##### `validate_path(path)`

- **Description**: Validates if the given path has a ".csv" file extension.

- **Parameters**:
  - `path` (str): The path to be validated.

- **Returns**:
  - `bool`: True if the path has a ".csv" extension, False otherwise.

##### `get_column_names(dataframe)`

- **Description**: Retrieves the column names from a Pandas DataFrame.

- **Parameters**:
  - `dataframe` (`pd.DataFrame`): The DataFrame from which to retrieve column names.

- **Returns**:
  - `list`: A list of column names.

##### `get_time_series(dataframe, column_name)`

- **Description**: Extracts the time series data from a specific column of a Pandas DataFrame.

- **Parameters**:
  - `dataframe` (`pd.DataFrame`): The DataFrame containing the time series data.
  - `column_name` (str): The name of the column to extract.

- **Returns**:
  - `np.array`: The time series data.

##### `sliceDataByTime(dataframe: np.array)`

- **Description**: (TODO) Slices data by time. (Not implemented)

- **Parameters**:
  - `dataframe` (np.array): The data array to be sliced.

- **Returns**:
  - `None`: Not applicable (TODO: Update after implementation).

#### Notes

- The `validate_path` function attempts to fix common issues with path strings (e.g., removing extra backslashes) but is currently not working. TODO

- Ensure that the necessary modules (`pandas` and `numpy`) are available and correctly imported.


## Conclusion

Summarize the main findings of the sensory data analysis. Discuss the implications of these findings and their significance in the broader context.

## Contributing

Explain how others can contribute to the project, whether through data collection, code development, or documentation improvements. Provide guidelines for reporting issues and submitting pull requests.

## License

Specify the project's license and provide information regarding its usage and distribution.

## Acknowledgements

Give credit to any individuals, organizations, or resources that contributed to the project or provided valuable support and insights.