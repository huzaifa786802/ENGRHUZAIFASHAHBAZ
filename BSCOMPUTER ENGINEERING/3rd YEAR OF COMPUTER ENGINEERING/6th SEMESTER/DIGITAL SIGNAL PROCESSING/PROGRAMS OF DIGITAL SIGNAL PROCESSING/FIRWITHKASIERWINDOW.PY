import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
# Define input specifications
wp = 0.375 * np.pi
ws = 0.5 * np.pi
# Calculate the order of the filter
N = int(np.ceil(8 * np.pi / (ws - wp)) + 1)
# Calculate the cutoff frequency
Wc = (wp + (ws - wp) / 2) / (0.5 * np.pi)
# Set the beta parameter for the Kaiser window
beta = 8
# Calculate the filter coefficients using the Kaiser window
h_kaiser = firwin(N, Wc, window=('kaiser', beta))
# Plot the frequency response
w, h = freqz(h_kaiser, worN=8000)
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(0.5 * w / np.pi, np.abs(h), 'b')
plt.title('Frequency response of the Kaiser Window FIR Filter')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude')
plt.grid()
# Plot the impulse response
plt.subplot(2, 1, 2)
plt.stem(h_kaiser, use_line_collection=True)
plt.title('Impulse response of the Kaiser Window FIR Filter')
plt.xlabel('Samples')
plt.ylabel('Amplitude')
plt.grid()
plt.tight_layout()
plt.show()