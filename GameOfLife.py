import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# start variables
game_size = 80
live_cells = 800

# create dataframe with zeroes (dead) and a few ones (live)
# borders will always be 0 (dead)
grid = pd.DataFrame(0, index=range(game_size), columns=range(game_size))
for _ in range(live_cells):
    grid.iloc[random.randrange(1, game_size - 1), random.randrange(1, game_size - 1)] = 1


# function checks state of surrounding cells and sums up live cells
def check_sum(x, y):
    neighborhood = grid.iloc[x - 1:x + 2, y - 1:y + 2]  # +2 instead of +1 as upper limit is not inclusive
    return neighborhood.values.sum() - grid.iloc[x, y]


# update function
# animation_cycle gets pushed by FuncAnimation and is necessary (is a running counter)
def update_image(animation_cycle):
    global grid
    grid_new = grid.copy()
    for x in range(1, game_size - 1):
        for y in range(1, game_size - 1):
            if grid.iloc[x, y] == 0 and check_sum(x, y) == 3:
                grid_new.iloc[x, y] = 1
            elif grid.iloc[x, y] == 1 and check_sum(x, y) != 2 and check_sum(x, y) != 3:
                grid_new.iloc[x, y] = 0

    print("Frame: " + str(animation_cycle + 1))
    grid = grid_new
    image.set_data(grid)

# start animation
fig, ax = plt.subplots(figsize=(8, 8))
image = ax.imshow(grid, cmap="Greys")
plt.axis('off')
ani = animation.FuncAnimation(fig, update_image, frames=200, repeat=False)

# save animation; frames/fps is video time in seconds
ani.save('GoL_animation.gif', fps=10, dpi=100)
print("Video saved. Process complete.")
