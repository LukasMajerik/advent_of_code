# https://adventofcode.com/2023/day/8#part2

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


# curr_pos = "AAA"
# print(curr_pos)
# steps = 0
# while curr_pos != "ZZZ":
#     steps += 1
#     curr_ins = ins.get_next_instruction()
#     curr_pos = map_.get(curr_pos)[0] if curr_ins == "L" else map_.get(curr_pos)[1]
#     # print(curr_ins, curr_pos)

# print("steps:", steps)


def is_the_end(positions):
    for pos in positions:
        if pos[2] != "Z":
            return False
    return True


nodes_end_with_A = [e for e in map_.keys() if e[2] == "A"]
print(nodes_end_with_A)


curr_pos = nodes_end_with_A[3:4]
print("curr_pos:", curr_pos)
steps = 0

while not is_the_end(curr_pos):
    steps += 1

    curr_ins = ins.get_next_instruction()
    # print(3 * "*")
    if steps % 100000 == 0:
        print(steps, curr_pos)
    for i in range(len(curr_pos)):
        cp = curr_pos[i]
        curr_pos[i] = map_.get(cp)[0] if curr_ins == "L" else map_.get(cp)[1]
        # print(curr_ins, cp)

print("steps:", steps)


# AAA 21409
# XDA 14363
# XSA 15989
# CFA 16531
# HJA 19241
# HPA 19783

print(21409 * 14363 * 15989 * 16531 * 19241 * 19783)


def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)


cycle_for_1st_arrival = [21409, 14363, 15989, 16531, 19241, 19783]

x = 21409
print(x, is_prime(x))
x = 14363
print(x, is_prime(x))
x = 15989
print(x, is_prime(x))
x = 16531
print(x, is_prime(x))
x = 19241
print(x, is_prime(x))
x = 19783
print(x, is_prime(x))

list_of_primes = []
for i in range(1, 21409 + 1):
    if is_prime(i):
        list_of_primes.append(i)

# print(list_of_primes)


def print_multipliers(x):
    multipliers = []
    for i in range(2, x + 1):
        if x % i == 0:
            multipliers.append(i)
            x /= i
    return multipliers


for x in cycle_for_1st_arrival:
    print(x, print_multipliers(x))

print(53 * 59 * 61 * 71 * 73 * 79 * 271)
