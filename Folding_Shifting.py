import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 6)


x = (n >= 0).astype(int)


x_fold = ((-n) >= 0).astype(int)


x_fold_shift = ((2 - n) >= 0).astype(int)

plt.figure(figsize=(10, 8))


plt.subplot(3, 1, 1)
plt.stem(n, x)
plt.title('x(n) = u(n)')
plt.grid(True)


plt.subplot(3, 1, 2)
plt.stem(n, x_fold)
plt.title('x(-n)')
plt.grid(True)


plt.subplot(3, 1, 3)
plt.stem(n, x_fold_shift)
plt.title('x(-(n-2)) = x(2-n)')
plt.grid(True)

plt.tight_layout()
plt.show()