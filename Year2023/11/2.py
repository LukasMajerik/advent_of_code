# https://adventofcode.com/2023/day/11

import os
from itertools import combinations

FILENAME = "data.txt"
# FILENAME = "data_test.txt"

EMPTY_SPACE = "."
GALAXY = "#"
EXPANSION_NUM = 1000000
# EXPANSION_NUM = 100
EXPANSION_SYMBOL = "X"

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))

data = f.read().split()

data = [list(e) for e in data]

for row in data:
    print(row)


class Universe:
    def __init__(self, field_map):
        self.field_map = field_map
        self.length = len(field_map)
        self.width = len(field_map[0])
        self.galax_pos = []

    def expand_non_galaxy_rows(self):
        for i in range(self.length - 1, -1, -1):
            row = self.field_map[i]
            if self.is_non_galaxy_row(row):
                for j, _ in enumerate(row):
                    self.field_map[i][j] = EXPANSION_SYMBOL

    def expand_non_galaxy_columns(
        self,
    ):
        for i in range(self.width - 1, -1, -1):
            if self.is_non_galaxy_column(i):
                self._expand_column(i)

    def _expand_column(self, column_num):
        for row in self.field_map:
            print("row:", row)
            row[column_num] = EXPANSION_SYMBOL

    def is_non_galaxy_row(self, row):
        print(f"Universe.is_non_galaxy_row({row})")
        return not any(e in [GALAXY] for e in row)

    def is_non_galaxy_column(self, column_num):
        column = []

        self._actualize_length()

        assert 0 <= column_num <= self.width - 1, "Column num out of range!"

        for j in range(self.length):
            column.append(self.field_map[j][column_num])

        print(
            f"Universe.is_non_galaxy_column({column_num})",
            "column:",
            column,
            not any(e in [GALAXY] for e in column),
        )
        return not any(e in [GALAXY] for e in column)

    def print(self):
        print("Universe.print()")
        for e in self.field_map:
            print(e)

    def _actualize_length(self):
        self.length = len(self.field_map)

    def get_shortest_dist_between_galax_pos(self, g1_pos, g2_pos):
        i1, j1 = g1_pos
        i2, j2 = g2_pos

        num_of_exp = self.get_num_of_expansions_between_galax_pos(g1_pos, g2_pos)

        field_map_dis = abs(i1 - i2) + abs(j1 - j2)

        return field_map_dis - num_of_exp + (num_of_exp * EXPANSION_NUM)

    def get_num_of_expansions_between_galax_pos(self, g1_pos, g2_pos):
        print(f"Universe.get_num_of_expansions_between_galax_pos({g1_pos},{g2_pos})")
        i1, j1 = g1_pos
        i2, j2 = g2_pos

        i1, i2 = sorted([i1, i2])
        j1, j2 = sorted([j1, j2])

        return self._get_num_of_expan_in_row(
            (j1, j2)
        ) + self._get_num_of_expan_in_column((i1, i2))

    def _get_num_of_expan_in_row(self, range_):
        i, j = range_
        row = self.field_map[0][i:j]
        print(f"Universe._get_num_of_expan_in_row({range_})", "row:", row)
        return sum(1 if e == EXPANSION_SYMBOL else 0 for e in row)

    def _get_num_of_expan_in_column(self, range_):
        i, j = range_
        column = [e[0] for e in self.field_map[i:j]]
        print(f"Universe._get_num_of_expan_in_column({range_})", "column:", column)
        return sum(1 if e == EXPANSION_SYMBOL else 0 for e in column)

    def list_galax_pos(self):
        for i, row in enumerate(self.field_map):
            for j, e in enumerate(row):
                if e == GALAXY:
                    self.galax_pos.append((i, j))

        print(self.galax_pos)

    def sum_shortest_gal_dist(self):
        self.list_galax_pos()
        sum_ = 0
        for pos_of_couple_gal in combinations(self.galax_pos, 2):
            pos1, pos2 = pos_of_couple_gal
            sum_ += self.get_shortest_dist_between_galax_pos(pos1, pos2)
            print(
                f"self.get_shortest_dist_between_galax_pos({pos1}, {pos2}):{self.get_shortest_dist_between_galax_pos(pos1, pos2)}"
            )
        return sum_


u = Universe(data)
u.expand_non_galaxy_rows()
u.expand_non_galaxy_columns()
u.print()
print("sum:", u.sum_shortest_gal_dist())
# print(u.get_shortest_dist_between_galax_pos((2, 0), (6, 9)))


# print([1, 2, 3, 4, 5][1:2])
