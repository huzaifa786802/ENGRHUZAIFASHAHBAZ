import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, ellip, freqz
# Filter specifications
order = 4
cutoff_freq = 0.2 # Normalized cutoff frequency
# Design the Butterworth filter
b_butter, a_butter = butter(order, cutoff_freq, btype='low', analog=False, output='ba')
# Design the Chebyshev Type I filter
rp_cheby1 = 1 # Passband ripple in dB
b_cheby1, a_cheby1 = cheby1(order, rp_cheby1, cutoff_freq, btype='low', analog=False, output='ba')
# Design the elliptic filter
rp_ellip = 1 # Passband ripple in dB
rs_ellip = 40 # Stopband attenuation in dB
b_ellip, a_ellip = ellip(order, rp_ellip, rs_ellip, cutoff_freq, btype='low', analog=False, output='ba')
# Compute the frequency response for each filter
w, h_butter = freqz(b_butter, a_butter)
w, h_cheby1 = freqz(b_cheby1, a_cheby1)
w, h_ellip = freqz(b_ellip, a_ellip)
# Plot the magnitude response for each filter
plt.figure()
plt.plot(w, np.abs(h_butter), label='Butterworth')
plt.plot(w, np.abs(h_cheby1), label='Chebyshev Type I')
plt.plot(w, np.abs(h_ellip), label='Elliptic')
plt.title('Magnitude Response')
plt.xlabel('Frequency (radians)')
plt.ylabel('Magnitude')
plt.legend()
plt.grid(True)
# Plot the phase response for each filter
plt.figure()
plt.plot(w, np.angle(h_butter), label='Butterworth')
plt.plot(w, np.angle(h_cheby1), label='Chebyshev Type I')
plt.plot(w, np.angle(h_ellip), label='Elliptic')
plt.title('Phase Response')
plt.xlabel('Frequency (radians)')
plt.ylabel('Phase (radians)')
plt.legend()
plt.grid(True)
plt.show()