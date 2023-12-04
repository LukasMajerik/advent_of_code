# https://adventofcode.com/2023/day/4

import os

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "data.txt"))

data = f.read().split("\n")


data_processed = []
i = 1
for row in data:
    row = row[row.find(":") + 2 :]
    row = row.split("|")
    # print(row)
    data_processed.append((row[0].split(), row[1].split()))


print(data_processed[0])

sum = 0
count_win_num = 0
for e in data_processed:
    for e2 in e[1]:
        if e2 in e[0]:
            count_win_num += 1

    sum += 2 ** (count_win_num - 1) if count_win_num > 0 else 0
    count_win_num = 0

print(sum)
