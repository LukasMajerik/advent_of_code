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


base = readFile()
def findNoundAndVerb():
    for x in range(0, 100):
        for y in range(0, 100):
            # print("ITERATION=================================")
            baseChild = [i for i in base]
            # print(hex(id(base)))
            # print(hex(id(baseChild)))
            # print('base: ', base[0], 'basechild: ', baseChild[0])
            baseChild[1] = x
            baseChild[2] = y
            # print(100*'*')
            # print(base)
            # print(100*'*')
            # print(baseChild)
            # print(100*'*')
            z = getIntcode(baseChild)
            # print(x, y, z[0])
            if z[0] == 19690720:
                return([x, y, z[0]])

print(findNoundAndVerb())
