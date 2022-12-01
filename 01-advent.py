# Part 1
with open("data/01-input.txt", "r") as file:
    lines = file.readlines()
    cal = 0
    calsums = []
    for line in lines:
        if len(line.strip()) == 0:
            calsums.append(cal)
            cal = 0
            continue
        cal += int(line.strip())
    
        
print(max(calsums))


# Part 2
print(sum(sorted(calsums)[-3:]))
