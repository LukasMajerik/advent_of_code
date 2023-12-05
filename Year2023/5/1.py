# https://adventofcode.com/2023/day/5

import os

FILENAME = "data.txt"
# FILENAME = "data_test.txt"


# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))

data = f.read().split("\n")

for row in data[0:1]:
    print(row)
    seeds = row[row.find(":") + 2 :].split()
    seeds = [int(e) for e in seeds]


# print(seeds)

print(88 * "*")
mapping = []
mappings = []

for row in data[2:]:
    print("row:", row)
    if row == "":
        print("adding mapping")
        mappings.append(mapping)
        mapping = []
    elif row.find(":") != -1:
        print("skipping row")
        pass
    else:
        print("appending to mapping")
        row = row.split()
        mapping.append([int(e) for e in row])

mappings.append(mapping)


print("mappings:", mappings)


class Mapping:
    def __init__(self, mapping):
        self.mapp_trans = []

        for e in mapping:
            f = (e[1], e[1] + e[2] - 1, e[0] - e[1])
            self.mapp_trans.append(f)

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

res = []
for e in seeds:
    for f in mappings_trans:
        e = f.trans(e)
    res.append(e)

print(min(res))
