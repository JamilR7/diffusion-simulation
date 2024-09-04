import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

grid_size = (11, 11)
grid = np.zeros(grid_size)
grid[5, 5] = 500

fig = plt.figure(facecolor="b")
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))

im = ax.imshow(grid, cmap='hot', interpolation='none', vmin=0, vmax=255)
ax.grid(color='white', linestyle='-', linewidth=0.5)

previous_grid = np.copy(grid)


def init():
    global previous_grid
    previous_grid = np.copy(grid)
    im.set_array(grid)
    return [im]


def diffusion(central, left, right, top, down):
    diffusion_factor = 0.1
    return central + diffusion_factor * (left + right + top + down - 4 * central)


def update_grid(frame):
    global previous_grid
    new_grid = np.copy(previous_grid)

    for i in range(1, grid_size[0] - 1):
        for j in range(1, grid_size[1] - 1):

            central = previous_grid[i, j]
            left = previous_grid[i, j - 1]
            right = previous_grid[i, j + 1]
            top = previous_grid[i - 1, j]
            down = previous_grid[i + 1, j]

            new_grid[i, j] = diffusion(central, left, right, top, down)

    grid[:] = new_grid
    previous_grid = np.copy(grid)

    im.set_array(grid)
    return [im]


animation = FuncAnimation(fig, update_grid, init_func=init, frames=1000, interval=25)

plt.show()
