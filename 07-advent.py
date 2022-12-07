# Part 1

# get structure of directories
# and size of each directory not including subdirectories
def map_dirs(file):
    current_dir = ""
    dirs = {}
    parent_dir = {}
    
    for line in file:
        if "$" in line:
            command = line.split(" ")
            if command[1] == "cd":
                arg = command[2]
                if arg == "..":
                    current_dir = parent_dir[current_dir]
                    #print(f"going up one level to dir {current_dir}")
                else:
                    # avoid top dir being "//"
                    if current_dir == "":
                        new_dir = current_dir + arg
                    else:
                        new_dir = current_dir + arg + "/"
                    
                    parent_dir[new_dir] = current_dir
                    
                    #print(f"going to dir {new_dir}")
                    if new_dir not in dirs:
                        dirs[new_dir] = 0
                    current_dir = new_dir
        elif not "dir" in line:
            output = line.split(" ")
            dirs[current_dir] += int(output[0])

    return (dirs, parent_dir)

# get sizes of child directories
def child_sums(dir, dirs, parent_dir):
    child_sum = 0
    for current_dir in dirs:
        if parent_dir[current_dir] == dir:
            child_sum += dirs[current_dir] + child_sums(current_dir, dirs, parent_dir)
    return(child_sum)


# map directories and add child sizes
def dir_sizes(file):
    dirs, parent_dir = map_dirs(file)
    
    for dir in dirs:
        dirs[dir] += child_sums(dir, dirs, parent_dir)
    return(dirs)

## Test with example data
with open("data/07-example.txt") as file:
    example = [line.strip() for line in file.readlines()]

sizes = [value for value in dir_sizes(example).values() if value < 100000]
print(sum(sizes))

# full input data
with open("data/07-input.txt") as file:
    commands = [line.strip() for line in file.readlines()]
sizes = dir_sizes(commands)
sizes_thresh = [value for value in sizes.values() if value < 100000]
print(sum(sizes_thresh))

# Part 2:

total_size = sizes["/"]
delete = 30000000 + total_size - 70000000

candidate_dirs = [value for value in sizes.values() if value > delete]
print(min(candidate_dirs))