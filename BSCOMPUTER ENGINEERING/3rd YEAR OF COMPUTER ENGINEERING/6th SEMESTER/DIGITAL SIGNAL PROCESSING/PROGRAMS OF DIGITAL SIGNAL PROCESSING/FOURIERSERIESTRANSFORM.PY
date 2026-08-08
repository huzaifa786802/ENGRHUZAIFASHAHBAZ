import numpy as np
import matplotlib.pyplot as plt
frequency=1000
sampling_freq=12000
duration=1
t=np.arange(0,duration,1/sampling_freq)
signal=np.cos(2*np.pi*frequency*t)
plt.stem(t,signal)
plt.xlabel('Time(s)')
plt.ylabel('Amplitude')
plt.title('Original SIganl')
plt.show()
exponentials=np.exp(1j*2*np.pi*frequency*t)
magnitudes=np.abs(exponentials)
angles=np.angle(exponentials)
manual_magnitudes=np.sqrt(np.real(exponentials)*2+np.imag(exponentials))
manual_angles=np.arctan2(np.imag(exponentials),np.real(exponentials))
print('Magnitudes(Built-in):',magnitudes[:10])
print('Magnitudes(Manual):',manual_magnitudes[:10])
print('Angles(Built-in):',angles[:10])
print('Angles(Manual):',manual_angles[:10])