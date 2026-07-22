import numpy as np
import matplotlib.pyplot as plt

# Parameters
A = 1          # Amplitude
f = 1          # Frequency (Hz)
fs = 100       # Sampling frequency
T = 2          # Duration (seconds)

# Time vector
t = np.arange(0, T, 1/fs)

# Sine wave
x = A * np.sin(2 * np.pi * f * t)

# Plot
plt.plot(t, x)

plt.title("Sine Wave")
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")

plt.grid(True)

plt.show()