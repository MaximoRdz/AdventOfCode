from collections import defaultdict
from heapq import heappop, heappush

"""
CONSTRAINS: 
1) 
Because it is difficult to keep the top-heavy crucible 
going in a straight line for very long, it can move at 
most three blocks in a single direction before it must 
turn 90 degrees left or right.
2)
The crucible also can't reverse direction; after 
entering each city block

Dijkstra algorithm already meets (2) by default
"""

with open("day-17/input.txt", "r") as file:
    data = file.read().split("\n")

grid = [[int(s) for s in row] for row in data]
    
NROWS = len(grid)
NCOLS = len(grid[0])
TARGET = NROWS-1, NCOLS-1


def node_neighbors(i, j):
    # generate neighbors iterable
    connections = ((0, -1), (-1, 0), (0, 1), (1, 0))
    for ci, cj in connections:
        if 0<=i+ci<NROWS and 0<=j+cj<NCOLS:
            yield i+ci, j+cj



# dijkstra algorithm
# nodes | dist | prev
# A     |   0  |  - 
# B     |  inf |  - 
# C     |  inf |  - 
            
visited = set()

starting_state = (0, 0, 0, 0, 0, 0)    # hl, i, j, dir_i, dir_j, current dir steps

pq = [starting_state]
path = defaultdict(tuple)

while pq:

    heatlost, i, j, di, dj, steps = heappop(pq)
    path[(i, j)] = di, dj

    if (i, j) == TARGET:
        print("Solution Part1: ", heatlost)
        break

    if (i, j, di, dj, steps) in visited:
        continue

    visited.add((i, j, di, dj, steps))

    if steps < 3 and (di, dj) != (0, 0):
        ni, nj = i+di, j+dj
        if 0<=ni<NROWS and 0<=nj<NCOLS:
            heappush(pq, (heatlost+grid[ni][nj], ni, nj, di, dj, steps+1))

    for ndi, ndj in ((0, -1), (-1, 0), (0, 1), (1, 0)):
        ni, nj = i+ndi, j+ndj
        if (ndi, ndj) != (-di, -dj) and (ndi, ndj) != (di, dj):
            if 0<=ni<NROWS and 0<=nj<NCOLS:
                heappush(pq, (heatlost+grid[ni][nj], ni, nj, ndi, ndj, 1))
    
    



# def plot_path():
#     # blocks_map = [[str(grid[i][j]) for j in range(NCOLS)] for i in range(NROWS)]    
#     blocks_map = [[" " for j in range(NCOLS)] for i in range(NROWS)]    

#     i, j = TARGET
#     c  = 0
#     while c < 1e3:
#         di, dj = path[(i, j)]
#         ni, nj = i-di, j-dj
#         blocks_map[ni][nj] = "#"
#         if(ni, nj) == (0, 0):
#             break
#         c+=1
#     print(*blocks_map, sep="\n")
#     return 0
# plot_path()

# print(path)








