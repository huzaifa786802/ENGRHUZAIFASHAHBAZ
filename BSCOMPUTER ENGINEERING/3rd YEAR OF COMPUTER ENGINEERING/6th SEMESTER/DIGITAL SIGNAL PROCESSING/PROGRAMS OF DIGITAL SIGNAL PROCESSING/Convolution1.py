#Convolution
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 3, 4, 5])
h = np.array([1, 1, 1])
def convolve(x, h): 
    y = np.convolve(x, h, mode='full') 
    return y
y = convolve(x, h)
plt.stem(x, label='Input signal')
plt.stem(h, label='Impulse response')
plt.stem(y, label='Output signal')
plt.legend()
plt.show() 