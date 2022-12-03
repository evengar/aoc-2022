# Part 1
import string

def split_string_half(string):
    nchar = len(string)
    if nchar % 2 == 0:
        midpoint = int(nchar/2)
        return (string[:midpoint], string[midpoint:])
    raise ValueError("Cannot split a string of uneven length in half")

print(split_string_half("AAAABB"))

# create dictionary for priority of characters
char_priority_dict = {}
n = 1
for char in string.ascii_lowercase + string.ascii_uppercase:
    char_priority_dict[char] = n
    n += 1

# returns the first matching char
# always only 1 in common
def find_common_char(str1, str2):
    for char in str1:
        if char in str2:
            return char
    return ""

def rucksackscores(rucksacks):
    score = 0
    for sack in rucksacks:
        str1, str2 = split_string_half(sack.strip())
        score += char_priority_dict[find_common_char(str1, str2)]
    return score

# read input and get answer
with open("data/03-input.txt") as f:
    rucksacks = f.readlines()

print(rucksackscores(rucksacks))

# part 2

# store all equal characters between two strings in a new string
def find_common_chars(str1, str2):
    result = ""
    for char in str1:
        if char in str2:
            result += char
            # remove the found char from strings in case they appear multiple times
            str2.replace(char, "")
    return result

# putting the functions together
def common_char_3(str1, str2, str3):
    common_12 = find_common_chars(str1, str2)
    # only 1 in common between all 3
    return(find_common_char(common_12, str3))

result = 0
for i in range(0, len(rucksacks), 3):
    group = [rucksacks[j].strip() for j in range(i, i+3)]
    common = common_char_3(group[0], group[1], group[2])
    result += char_priority_dict[common]
    
print(result)