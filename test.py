import numpy as np
import matplotlib.pyplot as plt


A = 10          # Amplitude
f = 1          # Frequency (Hz)
fs = 1000 
T = 5

x = np.arange(0, T, 1/fs)

y = A * np.sin(2* np.pi * f * x)

plt.plot(x, y)
plt.grid(True)
plt.title("Sine Wave")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.show()
