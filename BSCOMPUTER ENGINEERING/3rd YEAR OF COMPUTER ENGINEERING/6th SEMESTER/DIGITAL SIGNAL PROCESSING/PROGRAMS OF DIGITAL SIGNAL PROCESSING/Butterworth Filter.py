import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, freqz
# Filter specifications
order = 4
cutoff = 0.2  # Normalized frequency (0 to 1, where 1 is the Nyquist frequency)
# Design Butterworth filter
b_butter, a_butter = butter(order, cutoff, btype='low', analog=False)
# Frequency response
w, h = freqz(b_butter, a_butter, worN=8000)
# Plot frequency response
plt.figure(figsize=(12, 6))
plt.plot(w / np.pi, 20 * np.log10(abs(h)), 'b')
plt.title('Butterworth Filter Frequency Response')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.axvline(cutoff, color='red', linestyle='--', label=f'Cutoff frequency: {cutoff}')
plt.legend()
# Display the plot
plt.show()
# Print filter coefficients
print("Butterworth filter coefficients:")
print("b (numerator):", b_butter)
print("a (denominator):", a_butter)