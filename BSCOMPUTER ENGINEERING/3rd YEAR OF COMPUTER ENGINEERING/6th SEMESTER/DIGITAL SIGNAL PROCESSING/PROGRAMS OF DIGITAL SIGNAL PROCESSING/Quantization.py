import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from IPython.display import display, HTML
import scipy
t_min = -1
t_max = 1
num_t = 1000
t = np.linspace(t_min, t_max, num_t)
f = 2
xt = np.cos(2*np.pi*f*t)
plt.plot(t, xt)
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Plot of cos(2*pi*f*t)")
Fs = 5
Ts = 1/Fs
pulse_train = np.arange(t_min, t_max, Ts)
plt.stem(pulse_train, np.ones(len(pulse_train)))
plt.title("Plot of the pulse train")
plt.xlabel("t")
plt.ylabel("Amplitude")
xt_sampled = np.cos(2*np.pi*f*pulse_train)
plt.stem(pulse_train, xt_sampled)
plt.plot(t, xt, 'r')
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.title("Samples of x(t)")
plt.legend(["Samples of x(t)", "f(t)"])
x_rs, t_rs = scipy.signal.resample(xt_sampled, 1000, pulse_train)
plt.plot(t_rs, x_rs)
plt.stem(pulse_train, xt_sampled)
plt.plot(t, xt, 'r')
plt.title("Plot of recovered x(t)")
plt.xlabel("t")
plt.ylabel("Amplitude")
plt.legend(["Recovered x(t)", "Samples of x(t)", "f(t)"])