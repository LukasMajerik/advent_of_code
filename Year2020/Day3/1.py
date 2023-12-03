f = open("./data.txt", "r")
data = f.read().split()
# for row in data:
#     print(row)

print(len(data))
print(len(data[0]))

def position_x(step):
    return (step % len(data[0])+1)-1

def position_y(y):
    return y-1

# print(position_x(63))


def return_x_y(x, y):
    return data[y-1][x-1]


# l = ""
# print(55*"*")
# for i in range(1,63):
#     print(i)
#     l+=return_x_y(1,position_x(i))
# print(l)    
# print(55*"*")    

print(55*"-")
# for i in len(data):

num_trees=0
for i in range(1, len(data)):
    y=2*i+1
    if y >= len(data): break
    x=position_x(1*i+1)

    print(data[position_y(y)][:x-1] +"->"+ data[position_y(y)][x-1:])
    print(x, y, return_x_y(x, y))
    z = 1 if return_x_y(x, y)=="#" else 0
    num_trees+=z


print("number_of_trees", num_trees)



print("total_result", 87*169*99*98*53)