from heapq import heappop, heappush
from collections import defaultdict

# Your first task is to figure out which bricks are safe to disintegrate.
# A brick can be safely disintegrated if, after removing it, no other
# bricks would fall further directly downward.

with open("day-22/example.txt", "r") as file:
    data = file.read().splitlines()

blocks =  {}

max_x = 0
max_y = 0
max_z = 1



for i, line in enumerate(data): 
    st, nd = line.split("~")
    st = [int(c) for c in st.split(",")]
    nd = [int(c) for c in nd.split(",")]

    pos = "v"
    if st[2] == nd[2]:
        pos = "h"

    blocks[i] = [st, nd, pos]

print(blocks)





#     max_x = max(max_x, nd[0])
#     max_y = max(max_y, nd[1])
#     max_z = max(max_z, nd[2])


# for k in range(1, max_z+1):
#     for i in range(max_x+1):
#         for j in range(max_y+1):
#             # i, j, k







