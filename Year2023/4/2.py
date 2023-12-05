# https://adventofcode.com/2023/day/4#part2

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
    data_processed.append([1, row[0].split(), row[1].split()])

# for e in data_processed:
#     print(e)


data_processed_2 = []
count_win_num = 0
for e in data_processed:
    for e2 in e[2]:
        if e2 in e[1]:
            count_win_num += 1
    data_processed_2.append([1, count_win_num])
    count_win_num = 0

for i in range(len(data_processed_2)):
    # print(data_processed_2[i])
    for j in range(1, min(data_processed_2[i][1] + 1, len(data_processed_2) - 1)):
        data_processed_2[j + i][0] += data_processed_2[i][0]


print(88 * "*")
sum_ = 0
for e in data_processed_2:
    print(e)
    sum_ += e[0]

print("sum_:", sum_)
