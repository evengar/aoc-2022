# part 1

import numpy as np
import string

ex_grid = np.genfromtxt("data/12-example.txt", delimiter=1, dtype=str)
print(ex_grid)

height_dict = {}
for i, char in enumerate(string.ascii_lowercase):
    height_dict[char] = i

height_dict["S"] = height_dict["a"]
height_dict["E"] = height_dict["z"]

height_grid = np.vectorize(height_dict.get)(ex_grid)
print(height_grid)

def movable_tiles(grid, i, j):
    can_move = []
    adjacent = [(i, j+1), (i, j-1), (i+1, j), (i-1, j)]
    for pos in adjacent:
        if any(pos) < 0 or any(pos) > np.shape(movable_tiles)
