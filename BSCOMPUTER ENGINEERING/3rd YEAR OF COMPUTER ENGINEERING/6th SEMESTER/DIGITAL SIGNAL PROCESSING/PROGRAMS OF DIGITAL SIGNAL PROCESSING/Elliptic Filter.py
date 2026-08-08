import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, cheby1, ellip, freqz
order = 4  
cutoff = 0.3  
rp = 1  
rs = 40 
b_butter, a_butter = butter(order, cutoff, btype='low', analog=False)
w, h_butter = freqz(b_butter, a_butter)
b_cheby1, a_cheby1 = cheby1(order, rp, cutoff, btype='low', analog=False)
w, h_cheby1 = freqz(b_cheby1, a_cheby1)
b_ellip, a_ellip = ellip(order, rp, rs, cutoff, btype='low', analog=False)
w, h_ellip = freqz(b_ellip, a_ellip)
plt.figure()
plt.plot(w, np.abs(h_butter), label='Butterworth')
plt.plot(w, np.abs(h_cheby1), label='Chebyshev Type I')
plt.plot(w, np.abs(h_ellip), label='Elliptic')
plt.title('Magnitude Response')
plt.xlabel('Frequency (radians)')
plt.ylabel('Magnitude')
plt.legend()
plt.grid(True)
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