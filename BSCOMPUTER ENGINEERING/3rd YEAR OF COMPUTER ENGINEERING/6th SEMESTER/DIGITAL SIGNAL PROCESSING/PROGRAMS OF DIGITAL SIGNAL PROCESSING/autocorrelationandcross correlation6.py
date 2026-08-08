# autocorrelationandcross correlation
import numpy as np
import matplotlib.pyplot as plt
y= np.array([2,1,-2,1])
plt.subplot(1,2,1)
plt.stem(y) 
plt.xlabel('n')
plt.ylabel('y(n)')
plt.title('input sequence')
z = np.correlate(y, y, mode='full')
print('The values of z are = ')
print(z)
plt.subplot(1, 2, 2)
plt.stem(z)
plt.xlabel('n')
plt.ylabel('z(n)') 
plt.title('auto correlation of input sequence')
plt.show()