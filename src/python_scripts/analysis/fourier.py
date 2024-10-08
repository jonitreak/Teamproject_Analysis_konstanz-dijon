from matplotlib import pyplot as plt
import numpy as np
import pandas as pd



def smooth_signal(data, window_size):
    # Funktion für gleitenden Durchschnitt
    return data.rolling(window=window_size, min_periods=1).mean()

def perform_fourier_analysis(data, column_name, start_date, end_date,smoothing_window_size=3):
    column_values = data[column_name].str.replace(',', '.').astype(float)
    timestamps = pd.to_datetime(data['timestamp'].str[:19])
    start_date = np.datetime64(start_date)
    end_date = np.datetime64(end_date)

    # Glättung des Signals mit gleitendem Durchschnitt
    smoothed_column_values = smooth_signal(column_values, smoothing_window_size)

    time_diff_seconds = 15* 60
    # Filter data based on the specified date range
    mask = (timestamps >= start_date) & (timestamps <= end_date)
    smoothed_column_values = smoothed_column_values[mask]
    timestamps = timestamps[mask]
    if len(smoothed_column_values[mask]) % 2 != 0:
        smoothed_column_values = smoothed_column_values[1:len(smoothed_column_values[mask])]
        timestamps = timestamps[1:len(timestamps)]
    print(len(timestamps))

    # Perform Fourier transformation
    fft_result = np.fft.fft(smoothed_column_values)
    freqs = np.fft.fftfreq(len(timestamps), time_diff_seconds)
    print(freqs)
    print(abs(freqs))
    return freqs, fft_result, timestamps, smoothed_column_values

def filter_frequencies(freqs, fft_result):
    # Filter frequencies based on amplitude threshold
    threshold =  0.00003
    filtered_fft_result = fft_result
    filtered_freqs = freqs[np.abs(freqs) < threshold]
    filtered_fft_result[np.abs(freqs) > threshold]=0

    return filtered_freqs, filtered_fft_result

def inverse_fourier(filtered_freqs, filtered_fft_result, original_length):
    # Inverse Fourier transformation
    reconstructed_signal_complex = np.zeros(original_length, dtype=np.complex128)
    reconstructed_signal_complex = filtered_fft_result

    reconstructed_signal = np.fft.irfft(reconstructed_signal_complex,original_length)
    return reconstructed_signal

def identify_anomalies(original_data, reconstructed_data, threshold_multiplier=1):
    # Calculate the threshold based on a dynamic percentile that changes with the threshold_multiplier
    # This makes the threshold more sensitive to changes in the threshold_multiplier
    threshold = np.std(np.abs(original_data - reconstructed_data))*threshold_multiplier    
    anomalies = np.abs(original_data - reconstructed_data) > threshold

    print(f'Identified anomalies: {anomalies.sum()}')
    print('Threshold:', threshold)

    return anomalies, threshold

def visualize_reconstructed_data(ax, timestamps, original_data, reconstructed_data, anomalies, threshold):
    min_length = min(len(timestamps), len(reconstructed_data), len(original_data))

    ax.plot(timestamps[:min_length], original_data.iloc[:min_length], label='Originaldaten')
    ax.plot(timestamps[:min_length], reconstructed_data[:min_length], label='Rekonstruierte Daten', linestyle='--')

    # Plotte den Schwellenwert um die rekonstruierten Daten
    upper_threshold = reconstructed_data + threshold
    lower_threshold = reconstructed_data - threshold

    ax.fill_between(timestamps[:min_length], lower_threshold[:min_length], upper_threshold[:min_length], color='lightgreen', alpha=0.6, label='Schwellenwert')
    # Markiere Anomalien (Werte außerhalb des Schwellenwerts) mit roten Punkten
    ax.scatter(timestamps[:min_length][anomalies], original_data[:min_length][anomalies], color='red', label='Anomalien')

    # Füge Text mit der Anzahl der Anomalien hinzu
    ax.text(timestamps.iloc[0], max(original_data), f'Anzahl der Anomalien: {anomalies.sum()}', color='blue', fontsize=12)

    ax.set_title('Original vs. Reconstructed Data with Anomalies')
    ax.set_xlabel('Time')
    ax.set_ylabel('Value')
    ax.legend()
    ax.grid(True)

def do_fourier(data, column_name, start_date, end_date):
    freqs, fft_result, timestamps, column_values = perform_fourier_analysis(data, column_name, start_date, end_date)
    filtered_freqs, filtered_fft_result = filter_frequencies(freqs, fft_result)
    reconstructed_signal = inverse_fourier(filtered_freqs, filtered_fft_result, len(column_values))

    anomalies, threshold = identify_anomalies(column_values, reconstructed_signal)

    fig, ax = plt.subplots(figsize=(15, 5))
    ax.set_ylim(min(column_values), max(column_values))

    visualize_reconstructed_data(ax, timestamps, column_values, reconstructed_signal, anomalies, threshold)
    plt.tight_layout()
    plt.show()

