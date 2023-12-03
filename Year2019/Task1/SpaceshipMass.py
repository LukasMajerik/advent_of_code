class Mass:
    mass = 0

    def getMass(self, x):
        return x // 3 - 2

    def readFile(self):
        with open('Data.txt') as f:

            for line in f:
                self.mass += self.getMass(int(line))

        return(self.mass)

    def readFilePlusFuel(self):
        with open('Data.txt') as f:

            for line in f:
                self.mass += self.getMassPlusFuel(int(line))

        return(self.mass)

    def getMassPlusFuel(self, x):
        x = self.getMass(x)
        print("mass", self.mass)
        print("x:", x)
        if x <= 0:
            print("returnppppppppppppp", self.mass)
            return 5
            # return (self.mass)
        else:

            self.mass += x
            self.getMassPlusFuel(x)

    def returnSomething(self):
        return "something"

    def returnMass(self):
        return self.mass


x = Mass()
# print(x.readFile())
print("result:", x.getMassPlusFuel(1969))
# print(x.returnSomething())
# print(x.returnMass())
# print(x.readFilePlusFuel())
# print(x.returnMass())
