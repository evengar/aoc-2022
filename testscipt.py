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

xs = [[] for _ in range(9)]
print(xs)

for i in range(0, 36, 4):
        xs[int(i/4)].append([i, i+1, i+2])
for i in range(0, 36, 4):
        xs[int(i/4)].append([i, i+1, i+2])
print(xs)

x = [1] * 6
print(x[1::2])

y = [1,2,3]
y += [4,5,6]
print(y)

x = np.arange(10)
print(any(x > 5))
print(np.max(np.where(x > 5)))
