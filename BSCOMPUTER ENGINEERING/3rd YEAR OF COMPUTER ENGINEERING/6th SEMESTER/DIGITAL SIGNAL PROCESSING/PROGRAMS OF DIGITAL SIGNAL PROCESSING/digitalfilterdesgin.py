import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hamming, lfilter, freqz
np.random.seed(0)  # For reproducibility
fs = 700  # Sampling Frequency
t = np.linspace(0, 1.0, fs)  # Time vector
freq1 = 10  # Frequency of the first sine wave
freq2 = 80  # Frequency of the second sine wave
clean_signal = np.sin(2 * np.pi * freq1 * t) + np.sin(2 * np.pi * freq2 * t)
# Add noise
noise = np.random.normal(0, 0.5, clean_signal.shape)
noisy_signal = clean_signal + noise
# Step 2: Design the digital filter (low-pass FIR filter using window method)
cutoff = 10  # Desired cutoff frequency of the filter, Hz
nyquist = 0.5 * fs  # Nyquist frequency
normal_cutoff = cutoff / nyquist  # Normalized cutoff frequency
numtaps = 101  # Size of the FIR filter
# Use a Hamming window to design the filter
window = hamming(numtaps)
taps = np.sinc(2 * normal_cutoff * (np.arange(numtaps) - (numtaps - 1) / 2)) * window
taps /= np.sum(taps)  # Normalize the filter coefficients
# Step 3: Apply the filter to the noisy signal
filtered_signal = lfilter(taps, 1.0, noisy_signal)
# Step 4: Plot the results
plt.figure(figsize=(15, 10))
# Original signal
plt.subplot(3, 1, 1)
plt.plot(t, clean_signal)
plt.title('Original Signal')
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
# Noisy signal
plt.subplot(3, 1, 2)
plt.plot(t, noisy_signal)
plt.title('Noisy Signal')
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
# Filtered signal
plt.subplot(3, 1, 3)
plt.plot(t, filtered_signal)
plt.title('Filtered Signal')
plt.xlabel('Time [seconds]')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
# Plot frequency response of the filter
w, h = freqz(taps, worN=8000)
plt.figure()
plt.plot(0.5 * fs * w / np.pi, np.abs(h), 'b')
plt.title('Filter Frequency Response')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Gain')
plt.grid()
plt.show()