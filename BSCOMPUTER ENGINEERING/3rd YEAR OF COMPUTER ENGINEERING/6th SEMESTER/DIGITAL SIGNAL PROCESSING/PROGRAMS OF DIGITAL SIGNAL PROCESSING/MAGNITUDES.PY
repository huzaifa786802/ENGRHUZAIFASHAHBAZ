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
plt.title('Origianl Signal')
plt.show()
expoentials=np.exp(1j*2*np.pi*frequency*t)
magnitudes=np.abs(expoentials)
angles=np.angle(expoentials)
manual_magnitudes=np.sqrt(np.real(expoentials)*2+np.imag(expoentials))
manual_angles=np.arctan2(np.imag(expoentials),np.real(expoentials))
print('Magnitudes(Built-in):',magnitudes[:10])
print('Magnitudes(Manual):',manual_magnitudes[:10])
print('Angles(Built-in):',angles[:10])
print('Angles(Manual):',manual_angles[:10])