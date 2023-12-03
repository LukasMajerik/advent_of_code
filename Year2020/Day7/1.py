import re

# f = open("data.txt", "r")

# data = f.read().strip().split("\n\n")
# data = [r.split("\n") for r in data]


data = """light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags."""

data = data.split("\n")

bags = []
for r in data:
    bags.append(r[:r.find('bags')-1])
# print(bags)

data_contained = []
for r in data:
    data_contained.append(r[r.rfind('contain')+len('contain '):].strip('.').split(','))
# print(data_contained)
(print(55*"-"))
data_contained2 = []
for d in data_contained:
    bags_contained = []
    for e in d:
        bag_contained = []
        m = re.search(r"\d", e)
        if m:
            number = e[:m.end()].strip()
            bags_c = e[m.end():].strip()
            bags_c = bags_c.replace("bags","bag")
            bag_contained.append(number)
            bag_contained.append(bags_c)
        bags_contained.append(bag_contained)
    data_contained2.append(bags_contained)

# print(data_contained2)
(print(55*"-"))
data = []
for i in range(len(bags)):
    bag_desc = []
    bag_desc.append(bags[i])
    bag_desc.append(data_contained2[i])
    data.append(bag_desc)
print(data)

def has_bag(bagname):
    bagname += " bag"
    bags = []
    for bag_desc in data:
        # print("**", bag_desc[0])
        for bag_contained in bag_desc[1]:
            if bag_contained:
                # print(bag_contained[1])
                if bag_contained[1]==bagname:
                    bags.append(bag_desc[0])
    return bags




def find_bag(bagname):
    pass

print(has_bag('shiny gold'))
print(has_bag('bright white'))
print(has_bag('muted yellow'))


