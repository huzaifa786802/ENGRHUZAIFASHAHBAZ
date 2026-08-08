import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, freqz
from scipy.constants import pi
# Step I: Enter the pass band ripple (rp) and stop band ripple (rs)
rp = 0.1
rs = 40
# Step II: Enter the pass band frequency (wp) and stop band frequency (ws)
wp = 0.375 * pi
ws = 0.5 * pi
# Step III: Get the sampling frequency (fs)
fs = 2 * pi
# Step IV: Calculate normalized pass band frequency, and normalized stop band frequency w1 and w2 respectively
w1 = 2 * wp / fs
w2 = 2 * ws / fs
# Step V: Calculate the filter order
# Butterworth filter order
# [n, wn] = buttord(w1, w2, rp, rs)
# Chebyshev filter order
# [n, wn] = cheb1ord(w1, w2, rp, rs)
# Example filter order and wn values for demonstration
n = 6
wn = 0.4
# Step VI: Design an nth order digital low pass Butterworth or Chebyshev filter
# Butterworth filter
b, a = butter(n, wn)
# Chebyshev filter
# b, a = cheby1(n, rp, wn)
# Step VII: Find the digital frequency response of the filter
w, H = freqz(b, a)
# Step VIII: Calculate the magnitude of the frequency response in decibels (dB)
mag = 20 * np.log10(abs(H))
# Step IX: Plot the magnitude response [magnitude in dB Vs normalized frequency]
plt.figure(1)
plt.plot(w, mag)
plt.title('Magnitude Response')
plt.xlabel('Normalized Frequency')
plt.ylabel('Magnitude (dB)')
plt.grid(True)
# Step X: Calculate the phase response using angle(H)
phase = np.angle(H)
# Step XI: Plot the phase response [phase in radians Vs normalized frequency (Hz)]
plt.figure(2)
plt.plot(w, phase)
plt.title('Phase Response')
plt.xlabel('Normalized Frequency')
plt.ylabel('Phase (radians)')
plt.grid(True)
plt.show()