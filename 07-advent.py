# Part 1

## Exploring example data

with open("data/07-example.txt") as file:
    example = [line.strip() for line in file.readlines()]



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


# def add_to_parent(dir, visited_dirs):
#     if dir not in visited_dirs:
#         visited_dirs = visited_dirs.union({dir})
#         if parent_dir[dir] == "":
#             return
#         elif parent_dir[dir] == "/":
#             dirs[parent_dir[dir]] += dirs[dir]
#         else:
#             dirs[parent_dir[dir]] += dirs[dir]

#             add_to_parent(parent_dir[dir], visited_dirs)

def child_sums(dir, dirs, parent_dir):
    child_sum = 0
    for current_dir in dirs:
        if parent_dir[current_dir] == dir:
            child_sum += dirs[current_dir] + child_sums(current_dir, dirs, parent_dir)
    return(child_sum)


 
dirs, parent_dir = map_dirs(example)

def dir_sizes(file):
    dirs, parent_dir = map_dirs(file)
    
    for dir in dirs:
        dirs[dir] += child_sums(dir, dirs, parent_dir)
    return(dirs)

sizes = [value for value in dir_sizes(example).values() if value < 100000]
print(sum(sizes))





# real data:
with open("data/07-input.txt") as file:
    commands = [line.strip() for line in file.readlines()]
sizes = [value for value in dir_sizes(commands).values() if value < 100000]
print(sum(sizes))

# Part 2: