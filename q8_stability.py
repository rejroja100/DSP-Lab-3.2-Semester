import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-2, 21)
a_values = [0.5, 1.0, 1.2, -0.5]

plt.figure(figsize=(10, 8))
for i, a in enumerate(a_values, 1):
    x = np.where(n >= 0, a ** n, 0)
    plt.subplot(2, 2, i)
    plt.stem(n, x, basefmt=" ")
    stable = abs(a) < 1
    plt.title(f"h(n) = a^n u(n), a = {a}  |  {'Stable' if stable else 'Unstable'}")
    plt.xlabel("n")
    plt.ylabel("h(n)")
    plt.grid(True)

plt.tight_layout()
plt.show()

print("For h(n) = a^n u(n), the system is BIBO stable if |a| < 1.")
print("If a is real, then -1 < a < 1.")