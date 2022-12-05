# Part 1

crates = [[] for _ in range(9)]
instructions = []

with open("data/05-input.txt") as file:
    for line in file:
        if "[" in line:
            for i in range(0, len(line), 4):
                if not "   " in line[i:i+3]:
                    crates[int(i/4)].append(line[i:i+3])
        if "move" in line:
            instructions.append(line.strip())

#easier to work with if top crate is last in list
crates_rev = [x[::-1] for x in crates]


def parse_instructions(line):
    n, orig, dest = [int(x) for x in line.split(" ")[1::2]]
    return (n, orig, dest)

def move_crates(crates, instructions):
    n, orig, dest = parse_instructions(instructions)
    for i in range(n):
        crates[dest - 1].append(crates[orig - 1][-1])
        del crates[orig - 1][-1]
    return crates



def CrateMover9000(crates, instructions):
    for instruction in instructions:
        crates = move_crates(crates, instruction)
    return(crates)
final_crates = CrateMover9000(crates_rev, instructions)
result = "".join([crate[-1][1] for crate in final_crates])
print(result)

# Part 2

def move_crates_9001(crates, instructions):
    n, orig, dest = parse_instructions(instructions)
    batch = []
    for i in range(n):
        batch.append(crates[orig - 1][-1])
        del crates[orig - 1][-1]
    crates[dest - 1] += batch[::-1]
    
    return crates

def CrateMover9001(crates, instructions):
    for instruction in instructions:
        crates = move_crates_9001(crates, instruction)
    return(crates)

# make new crates_rev, because apparently it's being changed by the function??
# please help with understanding why :(
crates_rev = [x[::-1] for x in crates]


final_crates = CrateMover9001(crates_rev, instructions)
result = "".join([crate[-1][1] for crate in final_crates])
print(result)