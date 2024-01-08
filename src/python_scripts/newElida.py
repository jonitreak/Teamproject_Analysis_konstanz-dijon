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

     # Convert time differences to seconds
    time_diff_seconds = np.diff(timestamps).astype('timedelta64[s]').astype(float)

    # Filter data based on the specified date range
    mask = (timestamps >= start_date) & (timestamps <= end_date)
    temperatures = temperatures[mask]
    timestamps = timestamps[mask]

    # Perform Fourier transformation
    fft_result = np.fft.fft(temperatures)
    freqs = np.fft.fftfreq(len(timestamps), np.mean(time_diff_seconds))

    # Consider only positive frequencies
    positive_freqs = freqs[:len(freqs)//2]
    positive_fft_result = np.abs(fft_result)[:len(temperatures)//2]

    # Remove DC component
    #positive_fft_result[0] = 0

    # Find dominant frequency
    dominant_freq_index = np.argmax(positive_fft_result)
    dominant_freq = positive_freqs[dominant_freq_index]
    print(f'Dominant frequency: {dominant_freq: .4f} Hz')

    #time_array = np.arange(len(temperatures)) *15
    
    return positive_freqs, positive_fft_result

def inverse_fourier(signal_frequentiel):
    # Inverse Fourier transformation
    signal_temporel = np.fft.ifft(signal_frequentiel).real
    return signal_temporel

def identify_anomalies(fft_result, threshold_multiplier=1.5):
     # Calculate threshold as a multiple of the average amplitude of the dominant frequency
    threshold = threshold_multiplier * np.mean(fft_result)
    anomalies = fft_result > threshold
    print(f'Identified anomalies: {anomalies.sum()}')
    print('Threshold:', threshold)
    return anomalies


def visualize_fourier_analysis(ax, data, column_name, start_date, end_date):
    # Perform Fourier analysis
    freqs, fft_result = perform_fourier_analysis(data, column_name, start_date, end_date)

    # Identify anomalies
    anomalies = identify_anomalies(fft_result)

    # Filter timestamps for the specified date range
    mask = (data['timestamp'] >= start_date) & (data['timestamp'] <= end_date)

    # Plot Fourier analysis
    ax[0].plot(freqs, fft_result, label=f'Fourier Transform of {column_name}')
    ax[0].scatter(freqs[anomalies], fft_result[anomalies], color='red', label='Anomalies')
    ax[0].axhline(y=np.mean(fft_result), color='r', linestyle='--', label='Threshold')
    ax[0].set_title(f'Fourier Transform of {column_name} with Anomalies')
    ax[0].set_xlabel('Frequency (Hz)')
    ax[0].set_ylabel('Amplitude')
    ax[0].legend()
    ax[0].grid(True)

def visualize_transformed_data(ax, data, column_name, start_date, end_date):
    # Perform Fourier analysis
    freqs, fft_result = perform_fourier_analysis(data, column_name, start_date, end_date)

    # Reconstruct the signal using inverse Fourier transformation
    reconstructed_signal = inverse_fourier(fft_result)

    # Filter timestamps for the specified date range
    mask = (data['timestamp'] >= start_date) & (data['timestamp'] <= end_date)

    # Ensure that the lengths of timestamp series match
    # timestamps = data.loc[mask, 'timestamp'].values
    # reconstructed_timestamps = data.loc[mask, 'timestamp'].values[:len(reconstructed_signal)]
    timestamps = pd.to_datetime(data.loc[mask, 'timestamp'].str[:19])  # Convert to datetime with seconds
    reconstructed_timestamps = pd.to_datetime(data.loc[mask, 'timestamp'].str[:19])[:len(reconstructed_signal)]  
    

    # Plot the original and reconstructed data
    ax[1].plot(timestamps, data.loc[mask, column_name], label='Original Data')
    ax[1].plot(reconstructed_timestamps, reconstructed_signal, label='Reconstructed Data', linestyle='--')
    ax[1].set_title(f'Original vs. Reconstructed Data for {column_name}')
    ax[1].set_xlabel('Timestamp')
    ax[1].set_ylabel('Value')
    ax[1].legend()
    ax[1].grid(True)
    
def main():
    file_path = '/Users/elidavehapi/Documents/WS6/FranceProject/Teamproject_Analysis/src/data/daten.csv'

    data = pd.read_csv(file_path, decimal=',')

    # column_name = input('Enter the column name for analysis: ')
    # start_date = input('Enter the start date (YYYY-MM-DD): ')
    # end_date = input('Enter the end date (YYYY-MM-DD): ')
    # Specify the column name and date range
    column_name = 'RM_RBG_RAUMTEMPERATUR_POINT_ID_Value'
    start_date = '2021-02-01'
    end_date = '2021-04-20'

    # Create subplots
    fig, ax = plt.subplots(1, 2, figsize=(15, 6))

    # Visualize Fourier analysis
    visualize_fourier_analysis(ax, data, column_name, start_date, end_date)

    # Visualize transformed data
    visualize_transformed_data(ax, data, column_name, start_date, end_date)

    # Adjust layout for better spacing
    plt.tight_layout()
    
    # Show the plots
    plt.show()

if __name__ == "__main__":
    main()
