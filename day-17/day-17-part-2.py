from collections import defaultdict
from heapq import heappop, heappush

"""
CONSTRAINS: 
1) 
move a minimum of four blocks in that direction 
before it can turn (or even before it can stop 
at the end)
2)
move a maximum of ten consecutive blocks without turning.
"""

with open("day-17/input.txt", "r") as file:
    data = file.read().split("\n")

grid = [[int(s) for s in row] for row in data]
    
NROWS = len(grid)
NCOLS = len(grid[0])

# dijkstra algorithm
# nodes | dist | prev
# A     |   0  |  - 
# B     |  inf |  - 
# C     |  inf |  - 
            
visited = set()

starting_state = (0, 0, 0, 0, 0, 0)    # hl, i, j, dir_i, dir_j, current dir steps

pq = [starting_state]
path = defaultdict(tuple)

TARGET = NROWS-1, NCOLS-1
MAX_STEPS = 10
MIN_STOP = 4
while pq:

    heatlost, i, j, di, dj, steps = heappop(pq)
    path[(i, j)] = di, dj

    if (i, j) == TARGET and steps >= MIN_STOP:
        print("Solution Part 2: ", heatlost)
        break

    if (i, j, di, dj, steps) in visited:
        continue

    visited.add((i, j, di, dj, steps))

    if steps < MAX_STEPS and (di, dj) != (0, 0):
        ni, nj = i+di, j+dj
        if 0<=ni<NROWS and 0<=nj<NCOLS:
            heappush(pq, (heatlost+grid[ni][nj], ni, nj, di, dj, steps+1))

    if not (steps >= MIN_STOP or (di, dj) == (0, 0)):
        continue

    for ndi, ndj in ((0, -1), (-1, 0), (0, 1), (1, 0)):
        ni, nj = i+ndi, j+ndj
        if (ndi, ndj) != (-di, -dj) and (ndi, ndj) != (di, dj):
            if 0<=ni<NROWS and 0<=nj<NCOLS:
                heappush(pq, (heatlost+grid[ni][nj], ni, nj, ndi, ndj, 1))
else:
    print("No path found ...")
    








