#LINEARSYSTEMANDNONLINEARSYSTEM
import numpy as np
import matplotlib.pyplot as plt
def system(x):
    y = np.zeros_like(x)
    for n in range(len(x)):
        if n >= 2:
            y[n] = x[n] + 0.5 * x[n-2]
        else:
            y[n] = x[n]  
    return y
n = np.arange(0, 10)
x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x2 = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
y1 = system(x1)
y2 = system(x2)
y_sum = system(x1 + x2)
is_additive = np.allclose(y_sum, y1 + y2)
k = 2  # Scaling factor
y_scaled = system(k * x1)
is_homogeneous = np.allclose(y_scaled, k * y1)
plt.figure(figsize=(10, 6))
plt.subplot(2, 2, 1)
plt.stem(n, x1, label='x1[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.subplot(2, 2, 2)
plt.stem(n, x2, label='x2[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.subplot(2, 2, 3)
plt.stem(n, y_sum, label='y1[n] + y2[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.subplot(2, 2, 4)
plt.stem(n, y_scaled, label='k * y1[n]')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()
if is_additive and is_homogeneous:
    print("The system is linear.")
else:
    print("The system is not linear.")