# https://adventofcode.com/2023/day/6#part2

import os

FILENAME = "data.txt"
FILENAME = "data_test.txt"

# open file in the same directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, FILENAME))


data = f.read().split("\n")

data_processed = []

for row in data:
    row = row[row.find(":") + 1 :].split()
    data_processed.append([int(e) for e in row])

print(data_processed)


LENGTH = len(data_processed[0])
time = data_processed[0]
distance = data_processed[1]
print(time, distance)

way_to_win_all_races = 1
way_to_win = 0
for i in range(LENGTH):
    time_act = time[i]
    print("time_act:", time_act, 55 * "*")
    for j in range(time_act + 1):
        speed = j
        print("speed:", speed)
        time_left = time_act - j
        distance_act = speed * time_left
        if distance_act > distance[i]:
            way_to_win += 1
            print("way_to_win:", way_to_win)
    way_to_win_all_races *= way_to_win
    way_to_win = 0
    print("way_to_win_all_races:", way_to_win_all_races)

print(way_to_win_all_races)
