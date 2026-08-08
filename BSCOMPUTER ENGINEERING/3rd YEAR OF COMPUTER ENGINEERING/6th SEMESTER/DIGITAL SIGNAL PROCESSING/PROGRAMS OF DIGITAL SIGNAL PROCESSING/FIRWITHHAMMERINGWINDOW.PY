import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
# Input specifications
wp = 0.375 * np.pi
ws = 0.5 * np.pi
# Calculate the order of the filter
N = int(np.ceil(8 * np.pi / (ws - wp)) + 1)
# Calculate the cutoff frequency
Wc = (wp + (ws - wp) / 2) / (0.5 * np.pi)
# Calculate the filter coefficients using the Hamming window
h_hamming = firwin(N, Wc, window='hamming')
# Plot the frequency response
w, h = freqz(h_hamming, worN=8000)
plt.figure()
plt.title('Frequency Response')
plt.plot(w / np.pi, 20 * np.log10(np.abs(h)), 'b')
plt.ylabel('Amplitude [dB]', color='b')
plt.xlabel('Normalized Frequency [×π rad/sample]')
plt.grid()
plt.axvline(wp / np.pi, color='red', linestyle='--', label='wp')
plt.axvline(ws / np.pi, color='green', linestyle='--', label='ws')
plt.legend()
# Plot the impulse response
plt.figure()
plt.title('Impulse Response')
plt.stem(np.arange(N), h_hamming, basefmt=" ", use_line_collection=True)
plt.xlabel('Sample')
plt.ylabel('Amplitude')
plt.grid()
# Show the plots
plt.show()