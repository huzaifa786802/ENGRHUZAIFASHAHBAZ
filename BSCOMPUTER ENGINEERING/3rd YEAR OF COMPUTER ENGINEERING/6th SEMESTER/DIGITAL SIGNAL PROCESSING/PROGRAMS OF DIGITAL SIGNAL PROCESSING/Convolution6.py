# Convolution
import numpy as np
import matplotlib.pyplot as plt
def x(n):
    return (1/3)**(-n) * (n >= 0)
def h(n):
    return (n >= 1)
n = np.arange(-10, 10)
convolution_result = np.convolve(x(n), h(n), mode='full')
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.stem(n, x(n))
plt.title('Input Signal x(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 2)
plt.stem(n, h(n))
plt.title('Impulse Response h(n)')
plt.xlabel('n')
plt.ylabel('Amplitude')
conv_n = np.arange(n[0]*2, n[-1]*2 + 1)
plt.subplot(3, 1, 3)
plt.stem(conv_n, convolution_result)
plt.title('Convolution Result')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()