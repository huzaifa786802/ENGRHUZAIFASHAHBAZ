# autocorrelationandcross correlation
import numpy as np
import matplotlib.pyplot as plt
x=np.array([3,5,1,2])
h=np.array([1,4,3])
corr=np.convolve(x,h[::-1],mode='full')
lags=np.arange(-len(h)+1,len(x))
plt.stem(corr,lags)
plt.xlabel('Lag')
plt.ylabel('Cross correlation')
plt.title('Cross correlation of x(n) and h(n)')
plt.grid()
plt.show()