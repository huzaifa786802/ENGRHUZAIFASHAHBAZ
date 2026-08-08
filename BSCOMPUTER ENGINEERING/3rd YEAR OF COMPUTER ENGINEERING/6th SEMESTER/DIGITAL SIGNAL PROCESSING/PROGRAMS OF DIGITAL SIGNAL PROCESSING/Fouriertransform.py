import numpy as np
import matplotlib.pyplot as plt
y=np.ones(5)
Y=np.fft.fft(y)
plt.subplot(2,1,1)
plt.stem(y)
plt.title('Input signal')
plt.subplot(2,1,2)
plt.stem(np.abs(Y))
plt.title('Magnitude of Fourier coefficients')
plt.tight_layout()
plt.show() 