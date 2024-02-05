# https://adventofcode.com/2023/day/5#part2

import os


FILENAME = "data.txt"
# FILENAME = "data_test.txt"


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
        self.mapp_trans_rev = []

        for e in mapping:
            f = (e[1], e[1] + e[2] - 1, e[0] - e[1])
            self.mapp_trans.append(f)
        self._sort()

    def _sort(self):
        self.mapp_trans.sort(key=lambda a: a[0])

    def _sort_rev(self):
        self.mapp_trans_rev.sort(key=lambda a: a[0])

    def trans(self, x):
        for e in self.mapp_trans:
            if e[0] <= x <= e[1]:
                return x + e[2]
        return x

    def trans_rev(self, x):
        for e in self.mapp_trans_rev:
            if e[0] <= x <= e[1]:
                return x + e[2]
        return x

    def _build_trans_rev(self):
        for e in self.mapp_trans:
            f = (e[0] + e[2], e[1] + e[2], -e[2])
            self.mapp_trans_rev.append(f)
        self._sort_rev()

    def __repr__(self):
        return f"Mapping(self.mapp_trans={self.mapp_trans})"


mappings_trans = {}

for i in range(len(mappings)):
    m = Mapping(mappings[i])
    mappings_trans.setdefault(i, m)
    print("***", m)

complexity = 1
for i in mappings_trans.keys():
    complexity *= len(mappings_trans.get(i).mapp_trans)
print("complexity:", complexity)

min_ = 10000000000
max_ = max([e[1] for e in seeds_trans])
# print("max_:", max_)

# min_input = None
# for e in seeds_trans:
#     print(e)
#     for f in range(e[0], e[1] + 1):
#         if f % 100000 == 0:
#             print(f)
#         f2 = f
#         for g in mappings_trans.keys():
#             # print("mappings_trans.keys() key:", g)
#             f2 = mappings_trans.get(g).trans(f2)
#         if f2 < min_:
#             min_ = f2
#             min_input = f


print("reversed mappings:")
for e in mappings_trans.values():
    e._build_trans_rev()

for e in mappings_trans.values():
    print(e.mapp_trans_rev)


# print("test of reverse:")
# f2 = 46
# for j in range(max(mappings_trans.keys()), 0 - 1, -1):
#     print("f2 before trans_rev():", f2)
#     print(mappings_trans[j])
#     f2 = mappings_trans.get(j).trans_rev(f2)
# print("final res:", f2)


class Intervals:
    def __init__(self, intervals):
        self.intervals = intervals

    def is_in_intervals(self, x):
        for interval in self.intervals:
            if x in range(interval[0], interval[1] + 1):
                return True
        return False


print("seeds_trans:", seeds_trans)
seeds_trans_union = Intervals(seeds_trans)

# for i in range(max_):
#     f2 = i
#     if f2 % 100000 == 0:
#         print("f2:", f2)
#     for j in range(max(mappings_trans.keys()), 0 - 1, -1):
#         f2 = mappings_trans.get(j).trans_rev(f2)
#     if seeds_trans_union.is_in_intervals(f2):
#         print("minimum is:", f2)
#         break


# minimum is 3521067870 => find location

print("test of norm. order:", 88 * "*")
f2 = 3521067870
# f2 = 82
for g in mappings_trans.keys():
    print(f2)
    print(mappings_trans.get(g))
    f2 = mappings_trans.get(g).trans(f2)

print("res of norm. order:", f2)
