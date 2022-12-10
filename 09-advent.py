# Part 1
# Storing coordinates in numpy arrays
import numpy as np

# check if tail needs to be moved
def is_adjacent(head_pos, tail_pos):
    diff_array = tail_pos - head_pos
    
    return np.all(np.abs(diff_array) <= 1)

# translate movement from input
move_dict = {
    "R": np.array([0, 1]),
    "L": np.array([0, -1]),
    "U": np.array([1, 0]),
    "D": np.array([-1, 0])
}

# use sign of difference in position to determine tail movement
def move_tail(head_pos, tail_pos):
    diff_array = tail_pos - head_pos
    return -np.sign(diff_array)

# parse instructions and run simulation
def track_tail(instructions):
    head_pos = np.array([0, 0])
    tail_pos = np.array([0, 0])

    tail_visited = {tuple(tail_pos)}
    
    for instr in instructions:
        direction, steps = instr.split(" ")
        for steps in range(int(steps)):
            head_pos += move_dict[direction]
            if not is_adjacent(head_pos, tail_pos):
                tail_pos += move_tail(head_pos, tail_pos)
                tail_visited = tail_visited.union({tuple(tail_pos)})
    return len(tail_visited)

# test for example data

with open("data/09-example.txt") as f:
    example_instructions = [line.strip() for line in f.readlines()]

print(track_tail(example_instructions))

# try with full input data

with open("data/09-input.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

print(track_tail(instructions))

# part 2

# generalize to n tails following each other
def track_tail_n(instructions, n):
    positions = [np.array([0, 0]) for i in range(n)]
    tail_visited = {tuple(positions[-1])}
    
    for instr in instructions:
        direction, steps = instr.split(" ")
        for steps in range(int(steps)):
            positions[0] += move_dict[direction]
            for i in range(1, len(positions)):
                if not is_adjacent(positions[i-1], positions[i]):
                    positions[i] += move_tail(positions[i-1], positions[i])
            tail_visited = tail_visited.union({tuple(positions[-1])})
    return len(tail_visited)

print(track_tail_n(instructions, 10))