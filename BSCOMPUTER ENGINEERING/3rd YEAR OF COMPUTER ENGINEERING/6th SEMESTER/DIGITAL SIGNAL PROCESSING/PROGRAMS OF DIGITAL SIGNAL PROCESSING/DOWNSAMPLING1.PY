import numpy as np
import matplotlib.pyplot as plt
fs = 16000  
f1 = 55     
f2 = 60     
duration = 1  
t = np.arange(0, duration, 1/fs)
sine_wave = np.sin(2 * np.pi * f1 * t)
cosine_wave = np.cos(2 * np.pi * f2 * t)
original_signal = sine_wave + cosine_wave
downsampled_signal = np.zeros(2 * len(original_signal))
downsampled_signal[::2] = original_signal
plt.figure(figsize=(14, 6))
plt.subplot(2, 1, 1)
plt.plot(t, original_signal, label='Original Signal')
plt.title('Original Signal')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
t_downsampled = np.arange(0, 2 * duration, 1/fs)
plt.subplot(2, 1, 2)
plt.plot(t_downsampled, downsampled_signal, label='Downsampled Signal with Zero-Insertion')
plt.title('Downsampled Signal with Zero-Insertion')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()