import numpy as np
import matplotlib.pyplot as plt

grid_size = (100, 100)
grid = np.zeros(grid_size)

plt.imshow(grid, cmap='hot', interpolation='none')
plt.grid(True, color='white', linestyle='-', linewidth=0.5)
plt.show()