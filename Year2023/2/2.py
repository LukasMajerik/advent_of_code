# https://adventofcode.com/2023/day/2#part2

import os

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "data.txt"))

data = f.read().split("\n")
delimiters = [",", ";"]
COLORS = ["red", "green", "blue"]
data_processed = []

for row in data:
    row = row[row.find(":") + 2 :]
    for delimiter in delimiters:
        row = "|".join(row.split(delimiter))
    row = row.split("|")
    row = [e.strip().split() for e in row]
    data_processed.append(row)


def min_req_cubes_squared(game, colors=COLORS):
    square_color_cubes = 1
    for c in colors:
        color_filter = filter(lambda e: e[1] == c, game)
        filtered = list(color_filter)
        square_color_cubes *= max([int(e[0]) for e in filtered])
    return square_color_cubes


sum_square_cubes = 0
i = 0
for row in data_processed[:]:
    sum_square_cubes += min_req_cubes_squared(row)

print(sum_square_cubes)
