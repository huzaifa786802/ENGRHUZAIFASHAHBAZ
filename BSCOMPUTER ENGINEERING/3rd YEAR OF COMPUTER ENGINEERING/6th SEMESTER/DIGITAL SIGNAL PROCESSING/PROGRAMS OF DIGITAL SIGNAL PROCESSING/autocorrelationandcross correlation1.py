# autocorrelationandcross correlation
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
plt.subplot(1, 2, 1)
plt.stem(x)
plt.xlabel('n')
plt.ylabel('x(n)')
plt.title('input sequence')
# Auto-correlation of input sequence
z = np.correlate(x, x, mode='full')
print('The values of z are = ')
print(z)
plt.subplot(1, 2, 2)
plt.stem(z)
plt.xlabel('n')
plt.ylabel('z(n)') 
plt.title('auto correlation of input sequence')
plt.show()