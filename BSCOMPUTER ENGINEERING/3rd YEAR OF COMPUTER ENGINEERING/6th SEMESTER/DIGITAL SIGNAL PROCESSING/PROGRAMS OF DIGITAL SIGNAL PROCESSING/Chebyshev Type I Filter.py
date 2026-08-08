import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import cheby1, freqz
# Filter specifications
order = 4
ripple = 1  # in dB
cutoff_frequency = 0.2  # Normalized frequency (0 to 1, where 1 corresponds to Nyquist frequency)
# Design the Chebyshev Type I filter
b_cheby1, a_cheby1 = cheby1(order, ripple, cutoff_frequency, btype='low', analog=False)
# Compute the frequency response
w, h = freqz(b_cheby1, a_cheby1, worN=8000)
# Plot the frequency response
plt.figure(figsize=(10, 6))
plt.plot(0.5 * w / np.pi, 20 * np.log10(np.abs(h)), 'b')
plt.title('Chebyshev Type I Frequency Response')
plt.xlabel('Normalized Frequency')
plt.ylabel('Amplitude [dB]')
plt.ylim(-60, 5)
plt.grid()
plt.show()