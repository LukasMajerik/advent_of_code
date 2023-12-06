# https://adventofcode.com/2023/day/5#part2

import os

FILENAME = "data.txt"
FILENAME = "data_test.txt"


# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))


data = f.read().split("\n")

for row in data[0:1]:
    # print(row)
    seeds = row[row.find(":") + 2 :].split()
    seeds = [int(e) for e in seeds]


print("seeds:", seeds)


seeds_trans = []
for i in range(0, len(seeds), 2):
    # print("i:", i)
    seeds_trans.append((seeds[i], seeds[i] + seeds[i + 1] - 1))

seeds_trans.sort()
for e in seeds_trans:
    print("seeds_trans:", f"from:{e[0]:,}      to:{e[1]:,}")


print(88 * "*")
mapping = []
mappings = []

for row in data[2:]:
    # print("row:", row)
    if row == "":
        # print("adding mapping")
        mappings.append(mapping)
        mapping = []
    elif row.find(":") != -1:
        # print("skipping row")
        pass
    else:
        # print("appending to mapping")
        row = row.split()
        mapping.append([int(e) for e in row])

mappings.append(mapping)


# print("mappings:", mappings)


class Mapping:
    def __init__(self, mapping):
        self.mapp_trans = []

        for e in mapping:
            f = (e[1], e[1] + e[2] - 1, e[0] - e[1])
            self.mapp_trans.append(f)
        self._sort()

    def _sort(self):
        self.mapp_trans.sort(key=lambda a: a[0])

    def trans(self, x):
        for e in self.mapp_trans:
            if e[0] <= x <= e[1]:
                return x + e[2]
        return x

    def __repr__(self):
        return f"Mapping(self.mapp_trans={self.mapp_trans})"


mappings_trans = []

for e in mappings:
    m = Mapping(e)
    mappings_trans.append(m)
    print("***", m)

complexity = 1
for e in mappings_trans:
    complexity *= len(e.mapp_trans)
print("complexity:", complexity)

# min_ = 10000000000
# min_input = None
# for e in seeds_trans:
#     print(e)
#     for f in range(e[0], e[1] + 1):
#         # if f % 100000 == 0:
#         #     print(f)
#         print(f)
#         f2 = f
#         for g in mappings_trans:
#             # print(g)
#             f2 = g.trans(f2)
#         if f2 < min_:
#             min_ = f2
#             min_input = f

# print("min_:", min_, "min_input:", min_input)

# res = 79
# for e in mappings_trans:
#     res = e.trans(res)
# print("res:", res)


# 2.4 miliardy intervalov
# print(25 * 40 * 23 * 6 * 46 * 25 * 16)

# 38400 intervalov
# print(4 * 4 * 5 * 4 * 6 * 5 * 4)

# for i in range(10**9):
#     if i % 10000000 == 0:
#         print(i)
