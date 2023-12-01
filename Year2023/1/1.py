# https://adventofcode.com/2023/day/1#part2

import os

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "data.txt"))

data = f.read().split()

numbers = "1234567890"


def find_first_num(s, from_left=True):
    sequence = range(len(s)) if from_left else range(len(s) - 1, 0 - 1, -1)

    for i in sequence:
        if s[i] in numbers:
            return s[i]


sum = 0
for row in data:
    sum += int(find_first_num(row) + find_first_num(row, False))


print(88 * "*")
# data_r = data[3]
# print(data_r)
# print(find_first_num(data_r))
# print(find_first_num(data_r, False))

print(sum)
