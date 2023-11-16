import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def smooth_signal(time_series, window_size):
    smoothed_series = np.convolve(time_series, np.ones(window_size)/window_size, mode='same')
    return smoothed_series

def fourier_plot(time_series, intervall ):
    # number of scan points / samples
    N = len(time_series)

    # time intervall
    T = intervall

    # sampling frequency
    fs = 1.0 / T

    # frequencies for fourier anlaysis 
    frequencies = np.fft.fftfreq(N, T)

    # fourier
    fourier_transform = np.fft.fft(time_series)

    # Nur die positiven Frequenzen berücksichtigen (reale Werte) / positive values only
    positive_frequencies = frequencies[:N//2]
    positive_fourier = 2.0/N * np.abs(fourier_transform[:N//2])

    # Plot der Frequenzkomponenten / plot
    max_amplitude = np.max(positive_fourier)

    plt.figure(figsize=(10, 5))
    plt.plot(positive_frequencies, positive_fourier)
    plt.xlabel('Frequenz (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Fourier-Analyse')
    plt.grid(True)
    plt.ylim(0, max_amplitude)
    plt.show()
