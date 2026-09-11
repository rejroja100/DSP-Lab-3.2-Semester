import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11)
a_values = [0.5, 1.0, 1.5, -0.5]

plt.figure(figsize=(10, 8))
for i, a in enumerate(a_values, 1):
    x = np.where(n >= 0, a ** n, 0)
    plt.subplot(2, 2, i)
    plt.stem(n, x, basefmt=" ")
    plt.title(f"Exponential a^n u(n), a = {a}")
    plt.xlabel("n")
    plt.ylabel("x(n)")
    plt.grid(True)

plt.tight_layout()
plt.show()