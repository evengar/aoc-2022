# Part 1
with(open("data/10-input.txt")) as f:
    program = [line.strip() for line in f.readlines()]
    
cycle = 1
reg = 1
# reverse thresholds to be able to pop
thresholds = [20, 60, 100, 140, 180, 220][::-1]
vals = 0

for line in program:
    if line == "noop":
        cycle += 1
        if cycle > thresholds[-1]:
            vals += thresholds[-1] * reg
            thresholds.pop()

    else:
        cycle += 2
        if cycle > thresholds[-1]:
            vals += thresholds[-1] * reg
            thresholds.pop()
        reg += int(line.split()[1])
        
    if len(thresholds) == 0:
        break


print(vals)

# Part 2
def draw(cycle, reg):
    if cycle in [reg - 1, reg, reg + 1]:
        return "#"
    else:
        return "."

cycle = 0
reg = 1
output = ""

for line in program:
    if line == "noop":
        output += draw(cycle%40, reg)
    else:
        output += draw(cycle%40, reg)
        cycle += 1
        output += draw(cycle%40, reg)
        reg += int(line.split()[1])
    cycle += 1

out_format = ""
for i in range(0, len(output), 40):
    out_format += output[i:i+40] + "\n"
print(out_format)