#Convolution
import numpy as np
import matplotlib.pyplot as plt
x = np.array([1, 2, 4, 6, 8,9,10])
h = np.array([2, 1, 2])
def convolve(x, h): 
    y = np.convolve(x, h, mode='full') 
    return y
y = convolve(x, h) 
fig, axs = plt.subplots(3, 1, figsize=(8, 8), sharex=True) 
axs[0].stem(x)
axs[0].set_ylabel('Amplitude')
axs[0].set_title('Input Signal')
axs[1].stem(h)
axs[1].set_ylabel('Amplitude')
axs[1].set_title('Impulse Response')
axs[2].stem(y)
axs[2].set_xlabel('Sample Index')
axs[2].set_ylabel('Amplitude')
axs[2].set_title('Output Signal')
plt.tight_layout()
plt.show()