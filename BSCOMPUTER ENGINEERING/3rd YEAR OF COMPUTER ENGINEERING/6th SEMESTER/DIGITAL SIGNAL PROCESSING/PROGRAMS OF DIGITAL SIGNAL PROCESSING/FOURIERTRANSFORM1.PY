import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
def plot_signal(t, x, title):
    plt.figure()
    plt.stem(t[:100], x[:100])
    plt.title(title)
    plt.xlabel('Time [s]')
    plt.ylabel('Amplitude')
    plt.show()
def plot_spectrum(frequencies, X, title):
    magnitudes = np.abs(X)
    angles = np.angle(X)
    plt.figure()
    plt.stem(frequencies[:len(frequencies)//2], magnitudes[:len(frequencies)//2], use_line_collection=True)
    plt.title(f'Magnitude Spectrum of {title}')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Magnitude')
    plt.show()
    plt.figure()
    plt.stem(frequencies[:len(frequencies)//2], angles[:len(frequencies)//2], use_line_collection=True)
    plt.title(f'Phase Spectrum of {title}')
    plt.xlabel('Frequency [Hz]')
    plt.ylabel('Angle [rad]')
    plt.show()
# Part (a): Generate a Sinusoid
fs = 20000  
f = 2500    
t = np.arange(0, 1, 1/fs)  
x = np.sin(2 * np.pi * f * t)
plot_signal(t, x, 'Sinusoid (2.5 KHz)')
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(x), 1/fs)
plot_spectrum(frequencies, X, 'Sinusoid')
# Part (b): Generate a Square Wave
fs = 12000  
f = 1000    
t = np.arange(0, 1, 1/fs)  
x = signal.square(2 * np.pi * f * t)
plot_signal(t, x, 'Square Wave (1 KHz)')
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(x), 1/fs)
plot_spectrum(frequencies, X, 'Square Wave')
# Part (c): Generate a Sawtooth Wave
fs = 15000  
f = 3000    
t = np.arange(0, 1, 1/fs)  
x = signal.sawtooth(2 * np.pi * f * t)
plot_signal(t, x, 'Sawtooth Wave (3 KHz)')
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(x), 1/fs)
plot_spectrum(frequencies, X, 'Sawtooth Wave')
# Part (d): Generate a Triangle Wave
fs = 18000  
f = 1200    
t = np.arange(0, 1, 1/fs)  
x = signal.sawtooth(2 * np.pi * f * t, 0.5)
plot_signal(t, x, 'Triangle Wave (1.2 KHz)')
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(x), 1/fs)
plot_spectrum(frequencies, X, 'Triangle Wave')
# Part (e): Generate a Random Signal with Gaussian Distribution
fs = 6000  
t = np.arange(0, 1, 1/fs)  
x = np.random.normal(0, 1, len(t))
plot_signal(t, x, 'Random Signal with Gaussian Distribution')
X = np.fft.fft(x)
frequencies = np.fft.fftfreq(len(x), 1/fs)
plot_spectrum(frequencies, X, 'Random Signal')