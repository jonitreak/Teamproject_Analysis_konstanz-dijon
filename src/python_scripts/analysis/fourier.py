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

    time_diff_seconds = np.diff(timestamps).astype('timedelta64[s]').astype(float)

    # Filter data based on the specified date range
    mask = (timestamps >= start_date) & (timestamps <= end_date)
    smoothed_column_values = smoothed_column_values[mask]
    timestamps = timestamps[mask]

    # Perform Fourier transformation
    fft_result = np.fft.fft(smoothed_column_values)
    freqs = np.fft.fftfreq(len(timestamps), np.mean(time_diff_seconds))

    return freqs, fft_result, timestamps, smoothed_column_values

def filter_frequencies(freqs, fft_result, threshold_multiplier=1):
    # Filter frequencies based on amplitude threshold
    threshold =  threshold_multiplier * np.mean(np.abs(fft_result))
    filtered_freqs = freqs[np.abs(fft_result) > threshold]
    filtered_fft_result = fft_result[np.abs(fft_result) > threshold]

    return filtered_freqs, filtered_fft_result

def inverse_fourier(filtered_freqs, filtered_fft_result, original_length):
    # Inverse Fourier transformation
    reconstructed_signal_complex = np.zeros(original_length, dtype=np.complex128)
    reconstructed_signal_complex[:len(filtered_freqs)] = filtered_fft_result

    reconstructed_signal = np.fft.ifft(reconstructed_signal_complex).real

    return reconstructed_signal

def identify_anomalies(original_data, reconstructed_data, threshold_multiplier=2):
   # Ensure lengths match
    min_length = min(len(original_data), len(reconstructed_data))
    original_data = original_data[:min_length]
    reconstructed_data = reconstructed_data[:min_length]

    # Calculate the threshold based on the absolute difference
    threshold =  np.std(reconstructed_data)
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

