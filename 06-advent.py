# Part 1

with open("data/06-input.txt") as file:
    signal = file.readline()

for i in range(len(signal)):
    substr = signal[i:i+4]
    if len(set(substr)) == 4:
        print(i + 4)
        break

# part 2

for i in range(len(signal)):
    substr = signal[i:i+14]
    if len(set(substr)) == 14:
        print(i + 14)
        break