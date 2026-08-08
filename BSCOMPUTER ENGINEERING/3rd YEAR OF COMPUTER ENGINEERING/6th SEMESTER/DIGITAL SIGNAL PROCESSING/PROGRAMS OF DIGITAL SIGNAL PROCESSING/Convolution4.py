# Convolution
import numpy as np
import matplotlib.pyplot as plt
def h_n(n, a):
    return np.where(n >= 0, a ** n, 0)
def x_n(n, N):
    return np.where((n >= 0) & (n <= N), 1, 0)
def convolution(x, h):
    N1 = len(x)
    N2 = len(h)
    N = N1 + N2 - 1
    y = np.zeros(N)
    for n in range(N):
        for k in range(max(0, n - N2 + 1), min(N1, n + 1)):
            y[n] += x[k] * h[n - k]
    return y
a = 0.5
N = 10
n = np.arange(0, 2 * N)
x = x_n(n, N)
h = h_n(n, a)
y = convolution(x, h)
plt.figure(figsize=(10, 6))
plt.subplot(3, 1, 1)
plt.stem(n, x, label='$x(n)$')
plt.xlabel('$n$')
plt.ylabel('Amplitude')
plt.title('Input Signal')
plt.subplot(3, 1, 2)
plt.stem(n, h, label='$h(n)$', linefmt='r-', markerfmt='ro', basefmt='r-')
plt.xlabel('$n$')
plt.ylabel('Amplitude')
plt.title('Impulse Response')
plt.subplot(3, 1, 3)
plt.stem(np.arange(0, len(y)), y, label='$y(n)$', linefmt='g-', markerfmt='go', basefmt='g-')
plt.xlabel('$n$')
plt.ylabel('Amplitude')
plt.title('Output Signal')
plt.tight_layout()
plt.show()