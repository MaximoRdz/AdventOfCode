# Your first task is to figure out which bricks are safe to disintegrate.
# A brick can be safely disintegrated if, after removing it, no other
# bricks would fall further directly downward.
with open("day-22/input.txt", "r") as file:
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

count = 0
for i in range(len(bricks)):
    if all(len(supported_by[s]) >= 2 for s in supports[i]):
        count += 1
        
print("Solution Part 1: ", count)
# # map given a brick -> which b it supports & which b support it
# bricks_relations = {ind: {"supported_by":[],
#                           "supports": []}
#                           for ind in range(len(bricks))}

# for ind, block in enumerate(bricks):
#     min_z, max_z = block[2], block[5]
#     supported_by_ind = min_z-1
#     supports_ind = max_z+1

#     for supported_by in list(filter(lambda b: b[5]==supported_by_ind, bricks)):
#         # all the blocks below
#         if overlaps(block, supported_by):
#             bricks_relations[ind]["supported_by"].append(bricks.index(supported_by))

#     for supports in list(filter(lambda b: b[2]==supports_ind, bricks)):
#         if overlaps(block, supports):
#             bricks_relations[ind]["supports"].append(bricks.index(supports))


# disintegrable_blocks = 0

# for brick_ind, relations in bricks_relations.items():
#     # print(10*"---")
#     # print(f"Brick: [{brick_ind}]")
#     # print("Supports: ", relations["supports"])
#     # print("Supported by: ", relations["supported_by"])

#     if not relations["supported_by"]:
#         continue
#     if not relations["supports"]:
#         disintegrable_blocks += 1
#         continue

#     # one block can be removed if all b it supports are 
#     # also supported by b' != b
#     supports = relations["supports"]
#     for supports_ind in supports:
#         if not list(filter(lambda b: b!=brick_ind, bricks_relations[supports_ind]["supported_by"])):
#             break
#     else:
#         disintegrable_blocks += 1
    

# print("Solution Part 1: ", disintegrable_blocks)
