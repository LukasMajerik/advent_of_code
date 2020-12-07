# import re

# f = open("data.txt", "r")
# data = f.read().split("\n\n")
# print("data len: ", len(data))

# data = [r.split("\n") for r in data]

# data2 = []
# for r in data:
#     row = []
#     # print(r)
#     for details in r:
#         row+=(details.split(" "))
#     # print(row)    
#     data2.append(row)

# print("data2 len: ", len(data2))

# data3 = []
# for person in data2:
#     row2 = []
#     for detail in person:
#         a = list(detail.split(":"))
#         row2.append(a)
#     row2 = dict(row2)
#     data3.append(row2)

# # print(data3)

# print("data3 len: ", len(data3))
# print(150*"*")

# pattern = re.compile("^#[a-f0-9]+")

# passports_valid = 0
# iteration=0
# for passport in data3:
#     iteration +=1
#     # print(iteration, "========", passport, )
    
#     valid = 0
#     byr = passport.get('byr', '0')
#     if not(len(byr)==4 and int(byr) in range(1920, 2003)): 
#         # print("byr", byr)
#         valid +=1
#     iyr = passport.get('iyr', '0')        
#     if not(len(iyr)==4 and int(iyr) in range(2010, 2021)): 
#         # print("iyr", iyr)
#         valid +=1
#     eyr = passport.get('eyr', '0')
#     if not(len(eyr)==4 and int(eyr) in range(2020, 2031)): 
#         # print("eyr", eyr)
#         valid +=1

#     hgt = passport.get('hgt',None)
#     if hgt:
#             h = hgt
            
#             h1=""
#             h2="None"

#             start_cm = h.rfind('cm')
#             start_in = h.rfind('in')
            
#             if start_cm == -1 and start_in == -1:
#                 # print('1hgt', hgt, h1, h2)
#                 valid+=1
#             elif start_cm > -1:
#                 h1 = int(h[:start_cm])
#                 h2 = h[start_cm:]
#                 if h1 not in range( 150, 194):
#                     # print('2hgt', hgt, h1, h2)
#                     valid+=1
#             elif start_in > -1:
#                 h1 = int(h[:start_in])
#                 h2 = h[start_in:]
#                 if h1 not in range( 59, 77):
#                     # print('3hgt', hgt, h1, h2)
#                     valid+=1
#     else:
#         valid+=1
                

#     hcl = passport.get('hcl', "not-existing")

#     if not(pattern.fullmatch(hcl) and len(hcl)==7): 
#         # print("hcl", hcl)
#         # print(hcl)
#         valid +=1

#     ecl = passport.get('ecl', 'not-existing')        
#     if  ecl not in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'): 
#         # print("ecl", ecl)
#         valid +=1
    
#     pid = passport.get('pid', 'not-existing')
#     print(pid, '====')
#     if not(len(pid)==9 and pid.isdigit()): 
#         print(pid)
#         # print("pid", pid)
#         valid +=1

    
#     if valid == 0: passports_valid += 1
#     # print("VALID", valid, "VALID PASSPORTS:", passports_valid)
#     # passport.get('cid', None)


# print("valid passports:", passports_valid)