# https://adventofcode.com/2023/day/12

import os
import itertools

FILENAME = "data.txt"
# FILENAME = "data_test.txt"

OPERATIONAL = "."
DAMAGED = "#"
UNKNOWN = "?"
REPLACEMENT_SYMBOLS = (OPERATIONAL, DAMAGED)

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))

data = f.read().split("\n")

data_proc = []
for row in data:
    row = row.replace(",", " ").split(" ")
    row = (row[0], tuple(int(e) for e in row[1:]))
    data_proc.append(row)


# for e in data_proc:
#     print(e)


def how_many_valid_arrangements(row):
    print(row)
    formation, arrangement_operational = row
    num_of_uknown = formation.count(UNKNOWN)
    num_of_arangements = 0
    # print(num_of_uknown)

    for i, guess_arangement in enumerate(get_iter_product(num_of_uknown)):
        # print(i, guess_arangement)
        guess = replace_uknown_with_iter_product(formation, list(guess_arangement))
        if is_valid_arangement(guess, arrangement_operational):
            num_of_arangements += 1

    return num_of_arangements


def sum_valid_arrangements(data):
    sum_ = 0
    for row in data:
        sum_ += how_many_valid_arrangements(row)
    return sum_


def get_iter_product(length):
    return itertools.product(REPLACEMENT_SYMBOLS, repeat=length)


def is_valid_arangement(formation, arrangement_operational):
    len_arr_oper = len(arrangement_operational)

    formation = formation.split(".")
    formation = list_remove_empty_str(formation)

    # print(formation)
    if len(formation) != len_arr_oper:
        return False

    for i in range(len_arr_oper):
        if len(formation[i]) != arrangement_operational[i]:
            return False

    return True


def list_remove_empty_str(list_):
    return [e for e in list_ if e != ""]


def replace_uknown_with_iter_product(formation, iter_product):
    formation_guess = ""
    for e in formation:
        formation_guess += iter_product.pop(0) if e == UNKNOWN else e

    return formation_guess


# print(is_valid_arangement(".###.####...", (3, 2, 1)))
# print(
#     replace_uknown_with_iter_product(
#         "?###????????", [".", ".", ".", ".", ".", "#", "#", ".", "#"]
#     )
# )

print(how_many_valid_arrangements(data_proc[5]))
print(sum_valid_arrangements(data_proc))
