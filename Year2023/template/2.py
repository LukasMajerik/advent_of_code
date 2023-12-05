# https://adventofcode.com/2023/day/<day>#part2

import os

FILENAME = "data.txt"
FILENAME = "data_test.txt"

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))


data = f.read().split()

# for row in data:
#     print(row)
