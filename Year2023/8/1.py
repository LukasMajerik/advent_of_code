# https://adventofcode.com/2023/day/8

import os

FILENAME = "data.txt"
# FILENAME = "data_test.txt"

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))

data = f.read().split("\n")

for row in data[0:1]:
    instructions = row

print("instructions:", instructions)

data_processed = []
for row in data[2:]:
    row = row.replace("=", ",").replace("(", "").replace(")", "").replace(" ", "")
    row = row.split(",")
    data_processed.append(row)

print(data_processed)

map_ = {}
for e in data_processed:
    map_.setdefault(e[0], (e[1], e[2]))

print(map_)


class Instructions:
    def __init__(self, instructions):
        self.instructions = instructions
        self.position = -1

    def get_next_instruction(self):
        if self.position < len(self.instructions) - 1:
            self.position += 1
        else:
            self.position = 0

        return self.instructions[self.position]


ins = Instructions(instructions)


# for i in range(5):
#     print(i, Ins.get_next_instruction())


curr_pos = "AAA"
print(curr_pos)
steps = 0
while curr_pos != "ZZZ":
    steps += 1
    curr_ins = ins.get_next_instruction()
    curr_pos = map_.get(curr_pos)[0] if curr_ins == "L" else map_.get(curr_pos)[1]
    # print(curr_ins, curr_pos)

print("steps:", steps)
