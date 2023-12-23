

with open("day-14/input.txt", "r") as file:
    data = file.read().split("\n")
platform = [[c for c in row] for row in data]

class northPlatform:
    can_move = {"O": True, ".": False, "#": False}
    can_receive = {"O": False, ".": True, "#": False}
    def __init__(self, platform):
        self.NROWS = len(platform)
        self.NCOLS = len(platform[0])
        self.platform = platform
        self.rotate_platform = None

    def rotate_90(self):
        # clockwise rotation
        self.rotate_platform = []
        for j in range(self.NCOLS):
            self.rotate_platform.append([self.platform[i][j] for i in reversed(range(self.NROWS))])
        self.platform = self.rotate_platform


    def next(self):
        move = False
        for i in range(1, self.NROWS):
            for j in range(self.NCOLS):
                elem = self.platform[i][j]
                up_elem = self.platform[i-1][j]
                if self.can_move[elem] and self.can_receive[up_elem]:
                    self.platform[i][j] = "."
                    self.platform[i-1][j] = elem
                    move = True
        return move
                    
    def north(self):
        aux = True
        while aux: 
            aux = self.next()


    def cycle(self):
        for i in range(4):
            self.north()
            self.rotate_90()

    def load(self, northed=True):
        if northed:
            self.north()
        result = 0
        for i in range(0, self.NROWS):
            result += (self.NROWS - i) * self.platform[i].count("O")
        return result
    



obj = northPlatform(platform)

# print("Solution Part 1: ", obj.load())
t = 1
while t < 1e2:
    obj.cycle()
    print(t, obj.load(False))
    t += 1


