import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from IPython.display import display, HTML
Fs = 32000
T=1/Fs
t = np.arange(Fs//32)*T
w35 = 0.35*Fs/2
sine_35 = np.sin(2*np.pi*w35*t)
w40 = 0.4*Fs/2
sine_40 = 100*np.sin(2*np.pi*w40*t)
signal= sine_35 + sine_40
"""After sampling by a factor of N=4, still including the zeros, we get the following impluse train"""
unit = np.zeros(Fs//32)
unit[0::4]=1
signal_downsampled = signal*unit
plt.figure()
plt.plot(signal[0:100],'g')
plt.grid()
plt.xlabel('n')
plt.ylabel('Signal');
plt.show()
plt.stem(unit[0:100], use_line_collection=True)
plt.xlabel('n')
plt.ylabel('unit(n)');
plt.show()
plt.figure(figsize=(10,8))
plt.plot(signal[0:100], label='Original Signal')
plt.stem(signal_downsampled[0:100],linefmt='r',markerfmt='r.', use_line_collection=True,
label='Downsampled with zeros')
plt.show()