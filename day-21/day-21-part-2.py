from collections import deque

with open("day-21/input.txt", "r") as file:
    data = file.read().splitlines()


grid = []
for i, line in enumerate(data):
    grid.append([])
    for j, c in enumerate(line):
        grid[i].append(c)
        if c == "S":
            START = (i, j)

NROWS, NCOLS = len(grid), len(grid[0])

assert NROWS == NCOLS, "This is not a square grid"
N = NROWS

MAX_STEPS = 26501365
print("Grid Size: ", N, "Max steps: ", MAX_STEPS)
contained_grids = (2*MAX_STEPS + 1) // N
print("Large grid size can contain ", contained_grids, " NxN grids")
assert contained_grids % 2 == 1, "There is and even number of grids in the max allowed grid"

def reach(i0, j0, max_steps):
    q = deque([(i0, j0, max_steps)]) # state: i, j, steps
    garden_plots = {(i0, j0)}
    reached = set()

    while q:
        ci, cj, step = q.popleft()

        if step % 2 == 0:
            garden_plots.add((ci, cj))

        if step == 0:
            continue

        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ni = ci + di
            nj = cj + dj
            if not (0 <= ni < NROWS and 0 <= nj < NCOLS) or grid[ni][nj] == "#":
                continue
            if (ni, nj) in reached:
                continue
            q.append((ni, nj, step-1))
            reached.add((ni, nj))

    return len(garden_plots)

#                     E
#               O O E X E O O
#               O E X E X E O
#               E X E X E X E
#               O E X E X E O
#               O O E X E O O
#                     E  
# Edge cases 
# top, bottom, left and right
# partially filled diagonal grids
# inner grids: 
#     * 
# odd: 1, 8, 16 , 24, 46
#        7  8   8   22 
even = reach(*START, 2*N)
odd = reach(*START, 2*N+1)
print("Allowed states with even steps: ", even)
print("Allowed states with odd steps: ", odd)


