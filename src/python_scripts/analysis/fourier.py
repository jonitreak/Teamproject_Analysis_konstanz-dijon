from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

def perform_fourier_analysis(data, column_name, start_date, end_date):
 # Convert timestamps to datetime objects
    timestamps = pd.to_datetime(data['timestamp'].str[:10])

    # Convert start and end dates to datetime64[ns]
    start_date = np.datetime64(start_date)
    end_date = np.datetime64(end_date)

    # Filter data based on the specified date range
    mask = (timestamps >= start_date) & (timestamps <= end_date)
    filtered_data = data[mask]

    # Select the specified column and replace commas with periods, then convert to float
    column_values = filtered_data[column_name].str.replace(',', '.').astype(float)

    # Convert time differences to seconds
    time_diff_seconds = np.diff(timestamps[mask]).astype('timedelta64[s]').astype(float)

    # Perform Fourier transformation
    fft_result = np.fft.fft(column_values)
    freqs = np.fft.fftfreq(len(column_values), np.mean(time_diff_seconds))

    # Consider only positive frequencies
    positive_freqs = freqs[:len(freqs)//2]
    positive_fft_result = np.abs(fft_result)[:len(column_values)//2]

    # Find dominant frequency
    dominant_freq_index = np.argmax(positive_fft_result)
    dominant_freq = positive_freqs[dominant_freq_index]
    print(f'Dominant frequency: {dominant_freq: .4f} Hz')

    return positive_freqs, positive_fft_result

    #time_array = np.arange(len(column_values)) *15
    
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

    