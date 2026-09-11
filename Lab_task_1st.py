import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 1000)
f = 5

phase1 = np.sin(2*np.pi*f*t)
phase2 = np.sin(2*np.pi*f*t + 2 * np.pi / 3)
phase3 = np.sin(2*np.pi*f*t - 2 * np.pi / 3)

merged = phase1 + phase2 + phase3

plt.figure(figsize=(10, 6))
plt.plot(t, phase1, 'b-', linewidth=1.5, label='Phase 1')
plt.plot(t, phase2, 'g-', linewidth=1.5, label='Phase 2')
plt.plot(t, phase3, 'r:', linewidth=1.5, label='Phase 3')
plt.plot(t, merged, 'k-', linewidth=1.5, label='Merged (Sum)')

plt.title('Three phase sinusoidal signal - merged')
plt.xlabel("Time (t)")
plt.ylabel('Amplitude (V)')
plt.legend(loc='upper right')
plt.axhline(0, color='gray', linewidth=0.5)
plt.grid(False)
plt.tight_layout()
plt.show()