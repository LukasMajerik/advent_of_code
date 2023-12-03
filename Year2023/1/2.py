# https://adventofcode.com/2023/day/1#part2

import os

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "data.txt"))

data = f.read().split()


# EDGE CASES:!!!!!!!!!!!!!!
# The right calibration values for string "eighthree" is 83 and for "sevenine" is 79.


numbers = "1234567890"
numbers_spelled = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def find_first_num(s, from_left=True):
    sequence = range(len(s)) if from_left else range(len(s) - 1, 0 - 1, -1)

    for i in sequence:
        if s[i] in numbers:
            return s[i]


def numbers_spelled_first_n_nums(n):
    return [e[:n] for e in numbers_spelled]


def is_number_spelled(n):
    if n in numbers_spelled:
        return True
    return False


def is_substr_of_num_or_num(n, n_substr):
    if is_number_spelled(n):
        return 2
    if n in numbers_spelled_first_n_nums(n_substr):
        return 1
    return 0


# not working, as there can be 'twone' string and from that string result should be 2,
# not 1
def replace_spelled_by_num2(s):
    for i in range(len(numbers_spelled)):
        s = s.replace(numbers_spelled[i], str(i + 1))
    return s


def replace_spelled_by_num(s):
    s = s
    i, j = 0, 1
    while i <= len(s):
        while j <= len(s):
            # print("i:", i, "j:", j, "s[i:j]:", s[i:j])
            res = is_substr_of_num_or_num(s[i:j], j - i)
            if res == 2:
                # print("replacing num")
                num_idx = numbers_spelled.index(s[i:j])
                # s = s.replace(numbers_spelled[num_idx], str(num_idx + 1))
                s = s[0:i] + str(num_idx + 1) + s[i + 1 :]
                # print("new string:", s)
                i, j = 0, 1
            elif res == 1:
                j += 1
            else:
                i += 1
                j = i + 1
        i += 1
    return s


sum = 0
for row in data:
    print(row, 55 * "*")
    row = replace_spelled_by_num(row)
    print(row)
    first_num = find_first_num(row)
    second_num = find_first_num(row, False)
    print("first num:", first_num, "second_num:", second_num)
    print("first + sec num:", int(first_num + second_num))
    sum += int(first_num + second_num)
    print("sum:", sum)


# print(88 * "*")
# data_r = data[2]
# data_r = "eighthree"
# print(data_r)
# data_r = replace_spelled_by_num(data_r)
# print(data_r)
# sum += int(find_first_num(data_r)) + int(find_first_num(data_r, False))

print("sum:", sum)
