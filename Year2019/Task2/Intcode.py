def getIntcode(a) -> list:
    n = 0
    x = opCodeToFun(a[0+n])
    while x is not None:
        # print(x(a[a[1+n]], a[a[2+n]]))
        a[a[3+n]] = x(a[a[1+n]], a[a[2+n]])
        n += 4
        x = opCodeToFun(a[0+n])
    return a


def opCodeToFun(i):
    if i == 1:
        return lambda a, b: a + b
    if i == 2:
        return lambda a, b: a * b
    if i == 99:
        return None





def readFile():
    a = ''
    with open('Data.txt') as f:

        for line in f:
            a += line
    
    a = a.split(',')
    a = map(lambda x: int(x), a)
    print(a)
    return list(a)


# print(readFile())

# # a = [1, 0, 0, 0, 99]
# a = [2, 3, 0, 3, 99]
print(getIntcode(readFile()))