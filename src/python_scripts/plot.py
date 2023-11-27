import matplotlib.pyplot as plt
from fourierAnalysis import perform_fourier_analysis

def visualize_fourier_analysis(data, column_name, start_date, end_date, threshold_multiplier=2.0):
    # Perform Fourier analysis
    freqs, fft_result, threshold = perform_fourier_analysis(data, column_name, start_date, end_date, threshold_multiplier)

    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(freqs, fft_result, label='Fourier Transform of Room Temperature')
    plt.axhline(y=threshold, color='r', linestyle='--', label=f'Threshold (Multiplier={threshold_multiplier})')
    plt.title('Fourier Transform of Room Temperature with Threshold')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.legend()
    plt.grid(True)
    plt.show()

# Example usage:
# visualize_fourier_analysis(data, 'RM_ERRECHNETE_RAUMTEMPERATUR_DSP_POINT_ID_Value', '2021-01-30', '2021-04-15')
