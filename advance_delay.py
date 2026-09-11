import numpy as np
import matplotlib.pyplot as plt


n = np.arange(-5, 8)


u = (n >= 0).astype(int)


u_shift_right = (n >= 3).astype(int)


u_shift_left = (n >= -2).astype(int)

plt.figure(figsize=(10, 6))


plt.subplot(3, 1, 1)
plt.stem(n, u)
plt.title('x(n) = u(n)')
plt.grid(True)


plt.subplot(3, 1, 2)
plt.stem(n, u_shift_right)
plt.title('x(n-3) = u(n-3)')
plt.grid(True)


plt.subplot(3, 1, 3)
plt.stem(n, u_shift_left)
plt.title('x(n+2) = u(n+2)')
plt.grid(True)

plt.tight_layout()
plt.show()