## Part 1

with open("data/04-input.txt") as f:
    pairs = [line.strip().split(",") for line in f.readlines()]


def tasks_to_range(tasks):
    start, end = tasks.split("-")
    return(range(int(start), int(end) + 1))


overlap = 0
for pair in pairs:
    elf1 = set(tasks_to_range(pair[0]))
    elf2 = set(tasks_to_range(pair[1]))
    if elf1.issubset(elf2) or elf2.issubset(elf1):
        #print(elf1, elf2)
        overlap += 1
print(overlap)

## Part 2

# same as part1, but check for any intersections
overlap = 0
for pair in pairs:
    elf1 = set(tasks_to_range(pair[0]))
    elf2 = set(tasks_to_range(pair[1]))
    if len(elf1.intersection(elf2)) > 0:
        #print(elf1, elf2)
        overlap += 1
print(overlap)