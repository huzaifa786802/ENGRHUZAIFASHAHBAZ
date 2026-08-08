import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from IPython.display import display,HTML
fs=44100
f=400.0
s=np.sin(2*np.pi*f*np.arange(0,1,1.0/fs))
Omega=2*np.pi*f/fs
s1=np.sin(Omega*np.arange(0,fs,1))
plt.figure()
plt.plot(s[2:1000],'b')
plt.plot(s[1:1000],'r')
plt.grid()
unit=np.zeros(44100)
unit[0::8]=1
plt.figure()
plt.stem(unit[0:100])
plt.xlabel('n')
plt.ylabel('unit(n)')
sdu=s*unit
plt.figure(figsize=(10,8))
plt.plot(s[0:100], label='Original Signal')
plt.stem(sdu[0:100],linefmt='r',markerfmt='r.', use_line_collection=True,
label='Downsampled with zeros')
plt.legend()