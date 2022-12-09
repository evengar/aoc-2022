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
# move_dict = {
#     np.array([ 0, -2]): np.array([ 0,  1]),
#     np.array([ 0,  2]): np.array([ 0, -1]),
#     np.array([-2,  0]): np.array([ 1,  0]),
#     np.array([ 2,  0]): np.array([-1,  0]),

#     np.array([-2,  1]): np.array([ 1, -1]),
#     np.array([2, 1]): np.array([-1, -1]),
#     np.array([2, -1]): np.array([-1, 1]),
#     np.array([-2, -1]): np.array([1, 1]),
#     np.array([1, -2]): np.array([-1, 1]),
#     np.array([1, 2]): np.array([-1, -1]),
#     np.array([-1, 2]): np.array([1, -1]),
#     np.array([-1, -2]): np.array([1, 1])
# }

# this can be solved with math instead:

diff_array = np.array([0, -2])
move_array = np.array([1, 1])
print(move_array * -np.sign(diff_array))

diff_array = np.array([2, -1])
print(move_array * -np.sign(diff_array))

head_pos = np.array([0, 0])
tail_pos = np.array([2, 1])
diff_array = tail_pos - head_pos
tail_pos += move_array * -np.sign(diff_array)
print(tail_pos)

move_dict = {
    "R": np.array([0, 1]),
    "L": np.array([0, -1]),
    "U": np.array([1, 0]),
    "D": np.array([-1, 0])
}

def move_tail(head_pos, tail_pos):
    move_array = np.array([1, 1])
    diff_array = tail_pos - head_pos
    return move_array * -np.sign(diff_array)

with open("data/09-example.txt") as f:
    example_instructions = [line.strip() for line in f.readlines()]

head_pos = np.array([0, 0])
tail_pos = np.array([0, 0])

tail_visited = {tuple(tail_pos)}

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

print(track_tail(example_instructions))

# wow, it worked!
# try with full input data

with open("data/09-input.txt") as f:
    instructions = [line.strip() for line in f.readlines()]

print(track_tail(instructions))

# part 2

def track_tail_n(instructions, n):
    
    positions = [np.array([0, 0]) for i in range(n)]
    print(positions)
    tail_visited = {tuple(positions[-1])}
    
    for instr in instructions:
        direction, steps = instr.split(" ")
        for steps in range(int(steps)):
            positions[0] += move_dict[direction]
            for i in range(1, len(positions)):
                if not is_adjacent(positions[i-1], positions[i]):
                    positions[i] += move_tail(positions[i-1], positions[i])
            tail_visited = tail_visited.union({tuple(positions[-1])})
        #print(positions)
    return len(tail_visited)

print(track_tail_n(instructions, 10))