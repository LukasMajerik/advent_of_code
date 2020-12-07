import datetime

def readFile():
    a = ''
    with open('Data.txt') as f:
        i = 0
        for line in f:
            a += (line)

    # a = a.split(',')
    # a = map(lambda x: int(x), a)
    # print(a)
    return a


base = readFile()
print(200*'=')
# print(200*'=')
# print(base)
# print(200*'=')

# snake1 = base[0].split(',')
# snake2 = base[1].split(',')
# print(snake1)
# print(snake2)


# ===============================================================================================

a5 = """
R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83
"""
a6 = """
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7
"""


class MD:
    def __init__(self, instructions):

        aSplit = instructions.split('\n')
        aSplit = list(filter(lambda x: x != "", aSplit))
        self.snakeInstruc1 = aSplit[0].split(",")
        self.snakeInstruc2 = aSplit[1].split(",")
        self.snakePath1 = self.getPath(self.snakeInstruc1)
        self.snakePath2 = self.getPath(self.snakeInstruc2)
        self.intersectPath = (
            list(set(self.snakePath1) & set(self.snakePath2)))

    def getInstruc(self, s) -> list:
        a = (s[0], s[1:])
        return a

    def getPath(self, instrucs):
        currPos = [0, 0]
        path = []

        for i in instrucs:
            ins1 = self.getInstruc(i)[0]
            ins2 = int(self.getInstruc(i)[1])

            if ins1 == 'L':
                for i in range(0, ins2):
                    currPos[0] = currPos[0]-1
                    path.append((currPos[0], currPos[1]))
            elif ins1 == 'R':
                for i in range(0, ins2):
                    currPos[0] = currPos[0]+1
                    path.append((currPos[0], currPos[1]))
            elif ins1 == 'U':
                for i in range(0, ins2):
                    currPos[1] = currPos[1]+1
                    path.append((currPos[0], currPos[1]))
            elif ins1 == 'D':
                for i in range(0, ins2):
                    currPos[1] = currPos[1]-1
                    path.append((currPos[0], currPos[1]))
        return path

    def min(self):

        l = []
        for i in self.intersectPath:
            l.append(abs(i[0])+abs(i[1]))
        return min(l)

    def shortestInterection(self):
        l1 = []
        l2 = []

        for j in range(0, len(self.intersectPath)):

            t0 = self.intersectPath[j][0]
            t1 = self.intersectPath[j][1]
            t2 = min([i for i, v in enumerate(self.snakePath1)
                      if v == self.intersectPath[j]])
            t = (t0, t1, t2)
            l1.append(t)

        for j in range(0, len(self.intersectPath)):

            t0 = self.intersectPath[j][0]
            t1 = self.intersectPath[j][1]
            t2 = min([i for i, v in enumerate(self.snakePath2)
                      if v == self.intersectPath[j]])
            t = (t0, t1, t2)
            l2.append(t)
# 
        # print(l1)
        # print(l2)
        l3 = []
        for j in range(0, len(self.intersectPath)):
            t = (l1[j][0], l1[j][1], l1[j][2]+l2[j][2]+2)
            l3.append(t)
        # print(l3)
        aMin = [0, 0, 0]
        aMin[2] = l3[0][2]
        for j in range(0, len(self.intersectPath)):
            if l3[j][2] <= aMin[2]:
                aMin = [i for i in l3[j]]
        return(aMin)

t1 = datetime.datetime.now()
md = MD(readFile())
# md = MD(a6)
print("Min:", md.min())
print(200*"_")
print("check")
print(md.shortestInterection())
t2 = (datetime.datetime.now() - t1 )
print("elapsed time:", t2)