f = open("data.txt", "r")
data = f.read().split("\n\n")
data = [r.split("\n") for r in data]

data2 = []
for r in data:
    row = []
    # print(r)
    for details in r:
        row+=(details.split(" "))
    # print(row)    
    data2.append(row)

data3 = []
for person in data2:
    row2 = []
    for detail in person:
        a = list(detail.split(":"))
        row2.append(a)
    row2 = dict(row2)
    data3.append(row2)
    
print(150*"*")
print(data3[0])

passports_valid = 0
for passport in data3:
    valid = 0
    if passport.get('byr', None) is None: valid +=1
    if passport.get('iyr',None) is None: valid +=1
    if passport.get('eyr',None) is None: valid +=1
    if passport.get('hgt',None) is None: valid +=1
    if passport.get('hcl', None) is None: valid +=1
    if passport.get('ecl', None) is None: valid +=1
    if passport.get('pid', None) is None: valid +=1
    if valid == 0: passports_valid += 1
    # passport.get('cid', None)


print(passports_valid)
