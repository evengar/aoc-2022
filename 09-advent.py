# Part 1

import numpy as np

head_pos = np.array([0, 0])
tail_pos = np.array([0, 0])

def is_adjacent(head_pos, tail_pos):
    diff_array = tail_pos - head_pos
    
    return np.all(np.abs(diff_array) <= 1)

print(is_adjacent(head_pos, tail_pos))

print(is_adjacent(head_pos + 2, tail_pos))

print(tuple(np.array([2,1])))

# dict of how to move when not adjacent
move_dict = {
    np.array([ 0, -2]): np.array([ 0,  1]),
    np.array([ 0,  2]): np.array([ 0, -1]),
    np.array([-2,  0]): np.array([ 1,  0]),
    np.array([ 2,  0]): np.array([-1,  0]),

    np.array([-2,  1]): np.array([ 1, -1]),
    np.array([2, 1]): np.array([-1, -1]),
    np.array([2, -1]): np.array([-1, 1]),
    np.array([-2, -1]): np.array([1, 1]),
    np.array([1, -2]): np.array([-1, 1]),
    np.array([1, 2]): np.array([-1, -1]),
    np.array([-1, 2]): np.array([1, -1]),
    np.array([-1, -2]): np.array([1, 1])
}

head_pos = np.array([0, 0])
tail_pos = np.array([2, 1])

print(tail_pos + move_dict[tail_pos - head_pos])


