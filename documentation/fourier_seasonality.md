Removing seasonality from a time series using Fourier transformation is a technique that involves identifying and filtering out the frequency components corresponding to the seasonal patterns. Here's a more detailed explanation:

### Understanding Fourier Transform in the Context of Seasonality Removal

1. **Fourier Transform**: The Fourier Transform converts a time series from the time domain into the frequency domain. In the frequency domain, the time series is represented as a sum of sinusoids with different frequencies and amplitudes.

2. **Identifying Seasonal Frequencies**: Seasonal patterns in a time series correspond to specific frequencies. For example, a yearly seasonality in daily data shows a strong frequency at 1/365 cycles per day. In your case, with data measured every 15 minutes, you'll need to determine the frequency that corresponds to the seasonal cycle you wish to remove.

3. **Filtering Frequencies**: Once the frequencies corresponding to the seasonality are identified, they can be filtered out. This is done by setting the coefficients of these frequencies to zero in the frequency domain.

4. **Inverse Fourier Transform**: After filtering, apply the inverse Fourier Transform to convert the data back to the time domain. The resulting time series will have reduced or removed seasonality.

### Practical Steps in Python

1. **Perform Fourier Transform**: Use `scipy.fft.rfft` to transform the time series into the frequency domain.

2. **Identify and Remove Seasonal Frequencies**: Find the frequencies that correspond to the seasonal patterns and set their coefficients to zero. The exact frequencies to filter depend on the specifics of your data and the seasonality pattern.

3. **Apply Inverse Fourier Transform**: Use `scipy.fft.irfft` to transform the data back to the time domain.

### Example Python Function

Here's a conceptual function for seasonality removal using Fourier Transform. Note that identifying the exact frequencies to remove will require understanding the specific seasonality in your data.

```python
from scipy.fft import rfft, rfftfreq, irfft

def remove_seasonality_fft(data, freq_to_remove):
    # Perform Fourier Transform
    fft_result = rfft(data)

    # Frequencies corresponding to the data
    frequencies = rfftfreq(len(data), d=1/96)  # d is the sampling period (15min = 1/96 day)

    # Filter out the seasonal frequencies
    for freq in freq_to_remove:
        fft_result[(frequencies > freq - 0.001) & (frequencies < freq + 0.001)] = 0

    # Perform Inverse Fourier Transform
    return irfft(fft_result)
```

### Additional Considerations

- **Frequency Selection**: Identifying the right frequencies to remove is crucial. This often requires analyzing the Fourier Transform of your data and looking for peaks that correspond to seasonal patterns.
- **Sampling Period**: The `d` parameter in `rfftfreq` should match the sampling rate of your data. In your case, it's every 15 minutes, so 1/96 of a day.
- **Complexity of Seasonality**: Real-world data might have complex seasonality patterns that are not perfectly periodic or might have multiple overlapping seasonal cycles.

### Further Reading

For a deeper understanding and practical examples, these resources might be helpful:

- [Understanding the Fourier Transform](https://betterexplained.com/articles/an-interactive-guide-to-the-fourier-transform/)
- [Time Series Decomposition & Prediction in Python](https://towardsdatascience.com/time-series-decomposition-and-statsmodels-parameters-69e54d035453) (focuses on decomposition but offers a good insight into time series analysis).

Using Fourier Transform for anomaly detection and seasonality removal can be part of a comprehensive approach to preprocess your data for VAR (Vector Autoregression) analysis, ensuring that the inputs to your VAR model are as informative and clean as possible.