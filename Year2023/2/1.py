# https://adventofcode.com/2023/day/2

import os

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "data.txt"))

data = f.read().split("\n")
delimiters = [",", ";"]


def is_game_possible(game, constraint=[[12, "red"], [13, "green"], [14, "blue"]]):
    for c in constraint:
        color_filter = filter(lambda e: e[1] == c[1], game)
        filtered = list(color_filter)

        for e in filtered:
            if c[0] < int(e[0]):
                return False
    return True


data_processed = []

for row in data:
    row = row[row.find(":") + 2 :]
    for delimiter in delimiters:
        row = "|".join(row.split(delimiter))
    row = row.split("|")
    row = [e.strip().split() for e in row]
    data_processed.append(row)

sum_IDs = 0
i = 0
for row in data_processed:
    i += 1
    print(row)
    if is_game_possible(row):
        print(f"game {i} is possible")
        sum_IDs += i
print(sum_IDs)


game = [
    ["3", "blue"],
    ["4", "red"],
    ["1", "red"],
    ["2", "green"],
    ["6", "blue"],
    ["2", "green"],
]
