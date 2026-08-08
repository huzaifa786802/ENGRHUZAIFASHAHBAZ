# Convolution
import numpy as np
import matplotlib.pyplot as plt
def x(n):
    return (1/2)**n * (n >= 0)
def h(n):
    return (n >= 0) - (n >= 10)
def convolution(x, h):
    N = len(x) + len(h) - 1
    y = np.zeros(N)
    for n in range(N):
        for k in range(len(x)):
            if n - k >= 0 and n - k < len(h):
                y[n] += x[k] * h[n - k]
    return y
n = np.arange(0, 20)
xn = x(n)
hn = h(n)
yn = convolution(xn, hn)
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.stem(n, xn)
plt.title('Input Signal $x(n)$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 2)
plt.stem(n, hn)
plt.title('Impulse Response $h(n)$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.subplot(3, 1, 3)
plt.stem(np.arange(len(yn)), yn)
plt.title('Output Signal $y(n)$')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
