import numpy as np
import matplotlib.pyplot as plt

# ---------- Functional -> Graphical ----------
n = np.arange(-10, 11)
x_func = np.where((n >= 0) & (n <= 5), n, 0)

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.stem(n, x_func, basefmt=" ")
plt.title("Functional → Graphical: x(n) = n, 0 ≤ n ≤ 5")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.grid(True)

# ---------- Tabular -> Graphical ----------
n_tab = np.array([-2, -1, 0, 1, 2, 3, 4])
x_tab = np.array([0, 0, 1, 2, 3, 2, 1])

plt.subplot(1, 2, 2)
plt.stem(n_tab, x_tab, basefmt=" ")
plt.title("Tabular → Graphical")
plt.xlabel("n")
plt.ylabel("x(n)")
plt.grid(True)

plt.tight_layout()
plt.show()