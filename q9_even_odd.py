import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-10, 11)

# ---------------- Define your signal here ----------------
def x_signal(n):
    # Example: x(n) = n+1 for 0 <= n <= 4, else 0
    return np.where((n >= 0) & (n <= 4), n + 1, 0)
# ---------------------------------------------------------

x = x_signal(n)
x_even = 0.5 * (x_signal(n) + x_signal(-n))
x_odd  = 0.5 * (x_signal(n) - x_signal(-n))

plt.figure(figsize=(10, 8))

plt.subplot(3, 1, 1)
plt.stem(n, x, basefmt=" ")
plt.title("Original Signal x(n)")
plt.xlabel("n"); plt.ylabel("x(n)"); plt.grid(True)

plt.subplot(3, 1, 2)
plt.stem(n, x_even, linefmt="b-", markerfmt="bo", basefmt=" ")
plt.title("Even Part: xₑ(n) = 0.5·[x(n) + x(-n)]")
plt.xlabel("n"); plt.ylabel("xₑ(n)"); plt.grid(True)

plt.subplot(3, 1, 3)
plt.stem(n, x_odd, linefmt="r-", markerfmt="ro", basefmt=" ")
plt.title("Odd Part: xₒ(n) = 0.5·[x(n) - x(-n)]")
plt.xlabel("n"); plt.ylabel("xₒ(n)"); plt.grid(True)

plt.tight_layout()
plt.show()

# Verify x(n) = x_even(n) + x_odd(n)
print("Verification (x == x_even + x_odd):", np.allclose(x, x_even + x_odd))