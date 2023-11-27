from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def perform_fourier_analysis(data, column_name, start_date, end_date):
    # Select the specified column
    temperatures = data[column_name].astype(float)

    # Convert timestamps to datetime objects
    timestamps = pd.to_datetime(data['timestamp'].str[:10])

    # Convert start and end dates to datetime64[ns]
    start_date = np.datetime64(start_date)
    end_date = np.datetime64(end_date)

    # Filter data based on the specified date range
    mask = (timestamps >= start_date) & (timestamps <= end_date)
    temperatures = temperatures[mask]
    timestamps = timestamps[mask]

    # Convert time differences to seconds
    time_diff_seconds = np.diff(timestamps).astype('timedelta64[s]').astype(float)

    # Perform Fourier transformation
    fft_result = np.fft.fft(temperatures)
    freqs = np.fft.fftfreq(len(timestamps), np.mean(time_diff_seconds))

    # Consider only positive frequencies
    positive_freqs = freqs[:len(freqs)//2]
    positive_fft_result = np.abs(fft_result)[:len(fft_result)//2]

    # Remove DC component
    positive_fft_result[0] = 0

    # Find dominant frequency
    dominant_freq_index = np.argmax(positive_fft_result)
    dominant_freq = positive_freqs[dominant_freq_index]
    print(f'Dominant frequency: {dominant_freq} Hz')

    return positive_freqs, positive_fft_result

def main():
    # Load data from the text file and specify decimal separator
    file_path = '/Users/elidavehapi/Documents/WS6/FranceProject/Teamproject_Analysis/src/data/daten.csv'
    data = pd.read_csv(file_path, decimal=',')

    # Display available data range
    min_date = data['timestamp'].str[:10].min()
    max_date = data['timestamp'].str[:10].max()
    print(f'Data available from {min_date} to {max_date}')

    # Get user input for the column name
    column_name = input('Enter the column name for analysis: ')

    # Get user input for the date range
    start_date = input('Enter the start date (YYYY-MM-DD): ')
    end_date = input('Enter the end date (YYYY-MM-DD): ')

    # Perform Fourier analysis based on user input
    freqs, fft_result = perform_fourier_analysis(data, column_name, start_date, end_date)

    # Create a plot with x-axis from 0.0000 to 0.0002
    plt.figure(figsize=(10, 6))
    plt.plot(freqs, fft_result, label=f'Fourier Transform of {column_name}')

    # Highlight the range from 0.00000 to 0.00002
    plt.axvspan(0.00000, 0.00002, color='gray', alpha=0.3, label=f'Range from 0.00000 to 0.00002 Hz')

    plt.title(f'Fourier Transform of {column_name} with Range Highlighted')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
