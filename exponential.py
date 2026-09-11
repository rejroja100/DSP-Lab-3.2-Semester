import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 2, 3, 4, 5]


plt.stem(x,y)

plt.title('Exponential Growth')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.grid(True)
plt.show()