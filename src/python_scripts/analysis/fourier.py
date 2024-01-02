import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def perform_fourier_analysis(data: pd.DataFrame, column_name, start_date, end_date):
    # Select the specified column
    column_values = data[column_name].str.replace(',', '.').astype(float)

    # Convert timestamps to datetime objects
    timestamps = pd.to_datetime(data['timestamp'])

    # Filter data based on the specified date range
    mask = (timestamps >= start_date) & (timestamps <= end_date)
    column_values = column_values[mask]
    timestamps = timestamps[mask]

    # Convert time differences to seconds
    time_diff_seconds = np.diff(timestamps).astype('timedelta64[s]').astype(float)

    # Perform Fourier transformation in chunks
    chunk_size = 1024  # Adjust the chunk size as needed
    num_chunks = len(column_values) // chunk_size
    fft_result = np.zeros_like(column_values, dtype=np.complex128)

    for i in range(num_chunks):
        start_idx = i * chunk_size
        end_idx = (i + 1) * chunk_size
        subset = column_values[start_idx:end_idx]
        fft_result[start_idx:end_idx] = np.fft.fft(subset)

    # Handle the remaining part (if any)
    remaining_start = num_chunks * chunk_size
    fft_result[remaining_start:] = np.fft.fft(column_values[remaining_start:])

    freqs = np.fft.fftfreq(len(column_values), np.mean(time_diff_seconds))

    # Consider only positive frequencies
    positive_freqs = freqs[:len(column_values)//2]
    positive_fft_result = np.abs(fft_result)[:len(column_values)//2]

    # Find dominant frequency
    dominant_freq_index = np.argmax(positive_fft_result)
    dominant_freq = positive_freqs[dominant_freq_index]
    print(f'Dominant frequency: {dominant_freq} Hz')

    # Create a time array with the same length as column_values
    time_array = np.arange(len(column_values)) * 15

    return positive_freqs, positive_fft_result, time_array, column_values

def calculate_threshold(fft_result):
    # Calculate threshold as a multiple of the average amplitude of the dominant frequency
    threshold_multiplier = 2.0
    threshold = threshold_multiplier * np.mean(fft_result)
    print(f'Threshold: {threshold}')
    return threshold, threshold_multiplier

def inverse_fourier(signal_frequentiel):
    signal_temporel = np.fft.ifft(signal_frequentiel)
    return signal_temporel

def visualize_fourier_analysis(data: pd.DataFrame, column_name, start_date, end_date):
    # Perform Fourier analysis
    freqs, fft_result, time_array, column_values = perform_fourier_analysis(data, column_name, start_date, end_date)

    # Calculate and print threshold
    threshold, threshold_multiplier = calculate_threshold(fft_result)

    # Inverse Fourier Analysis back to the time domain
    fft_filtered = fft_result * (np.abs(fft_result) > threshold)
    fft_inversed = inverse_fourier(fft_filtered)

    # Plot
    plt.figure(figsize=(10, 6))
    
    # Ensure lengths match before plotting
    min_length = min(len(time_array), len(fft_inversed), len(column_values))
    
    plt.plot(time_array[:min_length], column_values[:min_length], color='b', label='Original Data')
    plt.plot(time_array[:min_length], fft_inversed[:min_length], label=f'Fourier Transform of {column_name}', color='g')
    plt.axhline(y=threshold, color='r', linestyle='--', label=f'Threshold (Multiplier={threshold_multiplier})')
    
    plt.title(f'Fourier Transform of {column_name} with Threshold')
    plt.xlabel('Time (Minutes)')
    plt.ylabel(column_name)
    plt.legend()
    plt.grid(True)
    plt.show()
