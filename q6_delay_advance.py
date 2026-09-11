import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11)

def x_base(n):
    # Example: x(n) = n+1 for 0 <= n <= 4, else 0
    return np.where((n >= 0) & (n <= 4), n + 1, 0)

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x_base(n), basefmt=" ")
plt.title("Original x(n)")
plt.xlabel("n"); plt.ylabel("x(n)"); plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, x_base(n - 3), basefmt=" ")
plt.title("x(n - 3): Delay by 3")
plt.xlabel("n"); plt.ylabel("x(n-3)"); plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, x_base(n + 2), basefmt=" ")
plt.title("x(n + 2): Advance by 2")
plt.xlabel("n"); plt.ylabel("x(n+2)"); plt.grid(True)

plt.tight_layout()
plt.show()