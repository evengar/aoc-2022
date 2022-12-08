# Part 1

import numpy as np

example_trees = np.genfromtxt("data/08-example.txt", delimiter = 1, dtype = "int8")
trees = np.genfromtxt("data/08-input.txt", delimiter = 1, dtype = "int8")


def is_visible(array, i, j):
    above = not any(array[:i, j] >= array[i, j])
    below = not any(array[i+1:, j] >= array[i, j])
    left = not any(array[i, :j] >= array[i, j])
    right = not any(array[i, j+1:] >= array[i, j])
    
    return above or below or left or right


def count_visible_trees(array):    
    visible_count = (array.shape[0] - 1) * 4
    for i in range(1, array.shape[0] - 1):
        for j in range(1, array.shape[1] - 1):
            visible = is_visible(array, i, j)
            if visible:
                visible_count += 1
    return visible_count

print(count_visible_trees(example_trees))
print(count_visible_trees(trees))

# Part 2

def scenic_score(array, i, j):
    current_tree = array[i, j]
    # store values to the sides of the current tree
    # reverse above and left arrays for simplicity
    above_array = array[:i, j][::-1]
    below_array = array[i+1:, j]
    left_array = array[i, :j][::-1]
    right_array = array[i, j+1:]
    if any(above_array >= current_tree):
        first_tree = np.min(np.where(above_array >= current_tree))
        above = first_tree + 1
    else:
        above = len(above_array)
    if any(below_array >= current_tree):
        first_tree = np.min(np.where(below_array >= current_tree))
        below = first_tree + 1
    else:
        below = len(below_array)
    if any(left_array >= current_tree):
        first_tree = np.min(np.where(left_array >= current_tree))
        left = first_tree + 1
    else:
        left = len(left_array)
    if any(right_array >= current_tree):
        first_tree = np.min(np.where(right_array >= current_tree))
        right = first_tree + 1
    else:
        right = len(right_array)
    
    return above * below * right * left

print(scenic_score(example_trees, 3, 2))
print(scenic_score(example_trees, 1, 2))

max_score = 0
for i in range(1, trees.shape[0] - 1):
    for j in range(1, trees.shape[1] - 1):
        score = scenic_score(trees, i, j)
        if score > max_score:
            max_score = score
print(max_score)

