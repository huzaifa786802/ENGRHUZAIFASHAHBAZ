import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
# Input specifications
wp = 0.375 * np.pi  # Passband edge frequency
ws = 0.5 * np.pi    # Stopband edge frequency
# Calculate the filter order
N = int(np.ceil(8 * np.pi / (ws - wp)) + 1)
# Calculate the cutoff frequency
Wc = (wp + (ws - wp) / 2) / (0.5 * np.pi)
# Calculate the filter coefficients using the Blackman window
h_blackman = firwin(N, Wc, window='blackman')
# Frequency response of the filter
w, h = freqz(h_blackman, worN=8000)
# Plotting the frequency response
plt.figure(figsize=(12, 6))
plt.subplot(2, 1, 1)
plt.plot(w / np.pi, 20 * np.log10(np.abs(h)), 'b')
plt.title('Frequency Response of the FIR Filter using Blackman Window')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Magnitude (dB)')
plt.grid()
plt.subplot(2, 1, 2)
plt.plot(w / np.pi, np.unwrap(np.angle(h)), 'r')
plt.xlabel('Normalized Frequency (×π rad/sample)')
plt.ylabel('Phase (radians)')
plt.grid()
plt.tight_layout()
plt.show()