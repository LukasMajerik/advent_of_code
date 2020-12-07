
ids = [992, 993, 994, 996, 997, 998]
min = min(ids)
max = max(ids)
print(min)
print(max)

ids_miss = []
for i in range(min, max):
    if i not in ids: ids_miss.append(i)
print(ids_miss)


