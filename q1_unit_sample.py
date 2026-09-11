import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11)
x = np.where(n == 0, 1, 0)

plt.stem(n, x)
plt.title("Unit Sample Sequence δ(n)")
plt.xlabel("n")
plt.ylabel("δ(n)")
plt.grid(True)
plt.show()