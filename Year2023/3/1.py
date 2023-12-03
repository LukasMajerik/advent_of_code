# https://adventofcode.com/2023/day/3

import os

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, "data.txt"))

data = f.read().split()

DATA_SPACE = "."
DATA_NUMBER = "1234567890"


class Number_In_Space:
    def __init__(self, number, start, end, y):
        self.number = number
        self.x_start = start
        self.x_end = end
        self.y = y

    def get_adjacent_locations_around_number(self):
        self.y1 = max(self.y - 1, 0)
        self.y2 = min(self.y + 1, HIGHT - 1)

        self.x1 = max(self.x_start - 1, 0)
        self.x2 = min(self.x_end + 1, WIDTH - 1)

    def is_number_adjacent_to_symbol(self):
        self.get_adjacent_locations_around_number()
        for i in range(self.y1, self.y2 + 1):
            for j in range(self.x1, self.x2 + 1):
                # print("Adjacent:", "i:", i, "j:", j)
                if data[i][j] not in (DATA_SPACE + DATA_NUMBER):
                    # print("It's symbol", data[i][j])
                    return True
        return False
    

    def __repr__(self):
        return f"Number_In_Space(self.number={self.number}, self.x_start={self.x_start}, self.x_end={self.x_end}, self.y={self.y})"


def get_number():
    pass


HIGHT = len(data)
WIDTH = len(data[0])
print("hight:", HIGHT, "width:", WIDTH)

do_once = 0


def get_

number = ""
sum = 0
for i in range(HIGHT):
    for j in range(WIDTH):
        curr_symbol = data[i][j]
        print("i:", i, "j:", j, "curr_symbol:", curr_symbol)
        if curr_symbol.isdigit():
            number += str(curr_symbol)
            if j == WIDTH - 1:
                print("number:", number)
                n = Number_In_Space(number, j - len(number), j - 1, i)
                if n.is_number_adjacent_to_symbol():
                    sum += int(n.number)
                number = ""
        elif number:
            print("number:", number)
            n = Number_In_Space(number, j - len(number), j - 1, i)
            if n.is_number_adjacent_to_symbol():
                sum += int(n.number)
            number = ""
print(sum)
# n = Number_In_Space():
