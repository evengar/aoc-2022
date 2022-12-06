## Script for testing that environment is properly set up, etc

import numpy as np
import string

print(np.zeros(10))

print(len(""))

# gives an error
# print(int(""))

print(3%2)
print(4%2)

print(set("abcdefg").intersection("gfkjkjkj"))

a = "abcd"
b = "bc"

print(b in a)

print(sum([True, False, True]))