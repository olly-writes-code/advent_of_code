from utils import get_input
import numpy as np


DAY = 3

input_data = [list(i) for i in get_input(DAY)]

start = np.array([0, 0])
max_width = len(input_data[0])
step = np.array([3, 1])
visited_locations = [i * step for i in range(len(input_data))]
tree_count = 0
for i in visited_locations:
    x = i[0] % len(input_data[0])
    y = i[1]
    if input_data[y][x] == "#":
        tree_count += 1
print(tree_count)
