import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

grid_size = (100, 100)
grid = np.zeros(grid_size)
grid[41:60, 41:60] = 200

fig = plt.figure(facecolor="b")
ax = plt.axes(xlim=(0, 100), ylim=(0, 100))

im = ax.imshow(grid, cmap='hot', interpolation='none', vmin=0, vmax=255)
ax.grid(color='white', linestyle='-', linewidth=0.5)


def update_grid(frame):
    print(frame)
    grid[40:61, 40:61] = 255 - frame

    im.set_array(grid)
    return [im]

animation = FuncAnimation(fig, update_grid, frames=256, interval=25)

plt.show()