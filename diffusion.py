import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

grid_size = (11, 11)
grid = np.zeros(grid_size)
velocity_x = np.zeros(grid_size)
velocity_y = np.zeros(grid_size)
x_index = 0
y_index = 0

fig = plt.figure(facecolor="g")
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))


def handleEvent(event):
    global previous_grid, x_index, y_index
    x_index = round(event.ydata)
    y_index = round(event.xdata)
    if event.button == 1 and 0 <= x_index < grid_size[1] and 0 <= y_index < grid_size[0]:
        print(x_index, y_index)
        grid[x_index, y_index] = 500
        velocity_y[x_index, y_index] = 5
        velocity_x[x_index, y_index] = 5
        previous_grid = np.copy(grid)

fig.canvas.mpl_connect('button_press_event', handleEvent)

im = ax.imshow(grid, cmap='hot', interpolation='none', vmin=0, vmax=255)
ax.grid(color='white', linestyle='-', linewidth=0.5)

previous_grid = np.copy(grid)

def init():
    #global previous_grid
    #previous_grid = np.copy(grid)
    im.set_array(grid)
    return [im]


def diffusion(central, left, right, top, down):
    diffusion_factor = 0.1
    return central + diffusion_factor * (left + right + top + down - 4 * central)


def advection():
    global x_index, y_index
    # Field_amount_for_target[cellPosition + current_cell_velocity * timestep]
    # = field_amount_for_current_cell
    print(f"Advection: x_index={x_index}, y_index={y_index}, velocity_y={velocity_y}, "
          f"velocity_x={velocity_x}")
    # we have a certain amount of dye in the cell we press
    # there should be a velocity in that cell holding the dye
    # based on that velocity, we locate the arrival cell
    # transport the dye to the new cell


def update_grid(frame):
    global previous_grid
    new_grid = np.copy(previous_grid)

    advection()

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
