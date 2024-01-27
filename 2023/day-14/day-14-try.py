from collections import defaultdict

with open("day-14/example.txt", "r") as file:
    data = file.read().split("\n")

platform = [[c for c in row] for row in data]


can_move = {"O": True, ".": False, "#": False}
can_receive = {"O": False, ".": True, "#": False}

NROWS = len(platform)
NCOLS = len(platform[0])

rocks = {}
n_rocks = 1

blocks = {}
n_block = 1

for i in range(NROWS):
    for j in range(NCOLS):
        if platform[i][j] == "O":
            rocks[n_rocks] = (i, j)
            n_rocks += 1
        elif platform[i][j] == "#":
            blocks[n_block] = (i, j)
            n_block += 1
        

def north(y, x):
    for i in range(y-1, -1, -1):
        if (i, x) in rocks.values() or (i, x) in blocks.values():
            return i+1, x
    return (0, x)

def south(y, x):
    for i in range(y+1, NROWS):
        if (i, x) in rocks.values() or (i, x) in blocks.values():
            return i-1, x
    return (NROWS-1, x)

        
def west(y, x):
    for j in range(x-1, -1, -1):
        if (y, j) in rocks.values() or (y, j) in blocks.values():
            return y, j+1
    return (y, 0)

def east(y, x):
    for j in range(x+1, NCOLS):
        if (y, j) in rocks.values() or (y, j) in blocks.values():
            return y, j-1
    return (y, NCOLS-1)

def load():
    result = 0
    for key, (y, x) in rocks.items(): 
        # sorted(rocks.items(), key=lambda values: values[1][0]):
        result += NROWS-y
        
    return result


def cycle():
    for key in rocks.keys():
        rocks[key] = north(*rocks[key])
    for key in rocks.keys():
        rocks[key] = west(*rocks[key])
    for key in rocks.keys():
        rocks[key] = south(*rocks[key])
    for key in rocks.keys():
        rocks[key] = east(*rocks[key])

rocks_init = rocks.copy()
for t in range(1, 100000):
    cycle()
    print(t)
    if sorted(rocks.values()) == sorted(rocks_init.values()):
        period = t
        print("the period is ", period)
        break
  


# def dict_to_map(rocks):
#     rocks_map = []
#     for i in range(NROWS):
#         rocks_map.append([])
#         for j in range(NCOLS):
#             rocks_map[i].append(".")
#             if (i, j) in rocks.values():
#                 rocks_map[i][j] = "O"
#             elif (i, j) in blocks.values():
#                 rocks_map[i][j] = "#"
#     return rocks_map
