import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = .5          
f = 10          
fs = 1000       
T = 1         

# Time vector
t = np.arange(0, T, 1/fs)

# Sine wave
x = A * np.sin(2 * np.pi * f * t)
y = A * np.sin(2 * np.pi * 1 * t +  np.pi)

# Plot
plt.plot(t, x)
plt.plot(t, y)

plt.title("Sine Wave")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.grid(True)

plt.show()