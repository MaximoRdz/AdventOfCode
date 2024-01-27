

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
        for _ in range(4):
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


visited = set()
obj.cycle()
visited.add(obj.load(False))
i = 1
N = int(1e9 -1) # len(sample)-1
cycle = []
while i<1e3:
    obj.cycle()
    current = obj.load(False)

    if current in visited:
        cycle.append(current)
        if len(cycle) > 4 and cycle[0]==cycle[-2] and cycle[1]==cycle[-1]:
            print("Cycle found", cycle[:-2])
            T = len(cycle[:-2]) 
            print("Period: ", T)
            tf = i-2
            print("tf: ", tf)
            break
    else:
        cycle.clear()
    # print(i, current, len(visited), cycle)
    i += 1
    visited.add(current)


print("Last index: ", N)
print("Total left values to compute: ", N-tf)
cycles = (N-tf)//T
print("Complete cycles contained: ", cycles)
ans = N - (tf+1+T*cycles)
print(ans)
print("Solution: ", cycle[ans])




