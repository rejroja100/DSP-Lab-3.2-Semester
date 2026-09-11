import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11)
x = np.where(n >= 0, n, 0)

plt.stem(n, x, basefmt=" ")
plt.title("Unit Ramp Signal r(n)")
plt.xlabel("n")
plt.ylabel("r(n)")
plt.grid(True)
plt.show()