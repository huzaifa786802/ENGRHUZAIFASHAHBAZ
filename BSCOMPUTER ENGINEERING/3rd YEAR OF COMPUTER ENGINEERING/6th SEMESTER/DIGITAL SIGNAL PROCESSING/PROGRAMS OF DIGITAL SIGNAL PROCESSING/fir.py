import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, freqz
wp = 0.375 * np.pi
ws = 0.5 * np.pi
wt = ws - wp
n1 = np.ceil(8 * np.pi / wt)
N = int(n1 + (n1 - 1) % 2)
print('Order of the FIR filter N =', N)
Wc1 = wp + wt / 2
fs = 2 * np.pi 
Wc = Wc1 / (0.5 * fs)
print('Cutoff frequency =', Wc) 
h = firwin(N, Wc, window='hamming')
print('Impulse Response of FIR filter:')
print(h)
plt.figure(1)
w, H = freqz(h)
plt.stem(w, np.abs(H))
plt.title('Frequency Response')
plt.xlabel('Frequency (radians)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.figure(2)
n = np.arange(N)
plt.stem(n, h)
plt.xlabel('n')
plt.ylabel('h(n)')
plt.title('Impulse Response of Filter')
plt.grid(True)
plt.show()