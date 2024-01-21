# Your first task is to figure out which bricks are safe to disintegrate.
# A brick can be safely disintegrated if, after removing it, no other
# bricks would fall further directly downward.
with open("day-22/example.txt", "r") as file:
    data = file.read().splitlines()


bricks = [[int(c) for c in line.replace("~", ",").split(",")] for line in data]
bricks.sort(key=lambda block: block[2])  # ascending z sorted


def overlaps(a, b):
    """
    checks whether two blocks overlap based on rectangle
    intersection on a 2d plane XY: 
    a := x in [x1, x2] ; y in [y1, y2]
    b := x in [x'1, x'2] ; y in [y'1, y'2]

    a intsersects b True 
            <=> 
    [x1, x2] intersects [x'1, x'2]
            and
    [y1, y2] intersects [y'1, y'2]
    """
    # x intersection and y intersection
    x_left = min(a, b, key=lambda pos: pos[0])
    x_right = max(a, b, key=lambda pos: pos[0])

    y_down = min(a, b, key=lambda pos: pos[1])
    y_up = max(a, b, key=lambda pos: pos[1])

    return  (x_left[3] >= x_right[0]) and (y_down[4] >= y_up[1])


assert overlaps([0, 1, 0, 2, 1, 0], [0, 1, 0, 2, 1, 0])==True

# drop each brick to the lowest place it can be without overlapping
for ind, block in enumerate(bricks):
    max_z = 1  # default min allowed z
    # all bricks below 
    for check in bricks[:ind]:
        if overlaps(block, check):
            max_z = max(max_z, check[5]+1) # running max 
    
    block[5] -= block[2] - max_z
    block[2] = max_z

bricks.sort(key=lambda block: block[2])

supported_by = {i: set() for i in range(len(bricks))} 
supports = {i: set() for i in range(len(bricks))} 

for j, upper in enumerate(bricks):
    for i, lower in enumerate(bricks[:j]):
        if overlaps(lower, upper) and lower[5]+1==upper[2]:
            supported_by[j].add(i) # j supported by i
            supports[i].add(j) # i supports j


# For each brick determine how many other would fall

count = 0
for i in range(len(bricks)):
    for s in supports[i]:
        if len(supported_by[s]) < 2:
            count += 1
        
print("Solution Part 2: ", count)

