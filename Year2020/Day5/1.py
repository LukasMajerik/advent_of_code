f = open("data.txt", "r")
data = f.read().strip().split("\n")

data.sort()
print(data)

# manually found
highest_id = 'BBBBBFFRRL'
print(len(highest_id))

rows = [ 2**i for i in range(0,7)][::-1]
columns = [2**i for i in range(0,3)][::-1]
print(rows)
print(columns) 

l = 'FBFBBFFRLR', 'BFFFBBFRRR', 'FFFBBBFRRR', 'BBFFBBFRLL', 'BBBBBFFRRL'
ids = []
for e in l:
    r_u = 128
    r_l = 1 
    for i in range(0, 7):
        if e[i]=='F': 
            r_u -= rows[i]
            
        else:
            r_l += rows[i]
        print("<",r_l - 1, ",",r_u - 1,">")
    row=r_l - 1
    print(55*"=")
    r_u = 8
    r_l = 1
    for i in range(7, 10):
        if e[i]=='L': 
            r_u -= rows[i-3]
        else:
            r_l += rows[i-3]
        print("<",r_l - 1, ",",r_u - 1,">")
    column=r_l-1
    id = row*8 + column
    ids.append(id) 
    print("ID:", id, 55*"=")
    print(55*"=")


ids.sort()
print(ids)
