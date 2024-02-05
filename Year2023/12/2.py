# https://adventofcode.com/2023/day/12

import os
import itertools

FILENAME = "data.txt"
FILENAME = "data_test.txt"

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
    row = row.split(" ")
    print(row[0])
    row_0 = ((row[0] + "?") * 5)[:-1]
    row_1 = ((row[1] + ",") * 5)[:-1]
    row = row_0 + " " + row_1
    row = row.replace(",", " ").split(" ")
    # print(row)
    # row[1:-1], -1 end position to remove last ","
    row = (row[0], tuple(int(e) for e in row[1:]))
    data_proc.append(row)

print("data_proc:")
for e in data_proc:
    print(e)
print()


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
    for i, row in enumerate(data):
        print(
            "sum_valid_arrangements():",
            i,
            row,
            val_arrang := how_many_valid_arrangements(row),
        )
        sum_ += val_arrang
    return sum_


def get_iter_product(length):
    return itertools.product(REPLACEMENT_SYMBOLS, repeat=length)


def is_valid_arrangement(formation, arrangement_operational):
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


def explore(formation, arrangement_operational):
    pos_explor = 0


class Expression:
    def __init__(self, exp: str, arran_operands: list):
        self.exp = exp
        self.arran_operands = arran_operands

    def find_valid_arran(self):
        s_e = SubExpression(self.exp, self.arran_operands[0])

        while not s_e.is_state_terminal():
            s_e.add_char()

    def __repr__(self) -> str:
        return f"Expression(self.exp = {self.exp}, self.arran_operands = {self.arran_operands})"


class SubExpression:
    def __init__(self, exp: str, arran_oper: int):
        self.exp = exp
        self.s_exp = ""
        self.arran_oper = arran_oper

    def add_char(self):
        # ako spracujeme expression?
        char = self.exp[0]

        if self.s_exp < self.arran_oper:
            if self.is_valid_addition(char):
                self.s_exp += char
                return True
        else:
            pass

    def is_valid_addition(self, char):
        if char != OPERATIONAL:
            return True
        return False

    def is_state_terminal(self):
        if self.s_exp[0] == DAMAGED:
            return True
        return False


# print(is_valid_arangement(".###.####...", (3, 2, 1)))
# print(
#     replace_uknown_with_iter_product(
#         "?###????????", [".", ".", ".", ".", ".", "#", "#", ".", "#"]
#     )
# )

# print(how_many_valid_arrangements(data_proc[5]))
# print(sum_valid_arrangements(data_proc))


exp, arran = data_proc[5]
exp, arran = ("?###????????", (3, 2, 1))
e = Expression(exp, arran)
print(e)
