from collections import deque, defaultdict

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
print((contained_grids // 2 + 1) * N)

def reach(i0, j0, max_steps):
    q = deque([(i0, j0, 0)]) # state i, j, steps
    garden_plots = {(i0, j0)}
    reached = {(i0, j0)}

    while q:
        ci, cj, step = q.popleft()

        if step % 2 == 0:
            garden_plots.add((ci, cj))

        if step == max_steps:
            continue

        for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            ni = ci + di
            nj = cj + dj
            if not (0 <= ni < NROWS and 0 <= nj < NCOLS) or grid[ni][nj] == "#":
                continue
            if (ni, nj) in reached:
                continue
            q.append((ni, nj, step+1))
            reached.add((ni, nj))

    return len(garden_plots)

#               O O O # O O O
#               O O # # # O O
#               O # # # # # O
#               O O # # # O O
#               O O O # O O O
# Edge cases 
# top, bottom, left and right
# partially filled diagonal grids
# inner grids: 
#     * 

# def periodic_boundaries(i, j):
#     # a // b = 0 a<b
#     # a // b = 1 b<=a<2b
#     # . . . 
#     ni = i - (i//N)*N
#     nj = j - (j//N)*N
#     return ni, nj 

# q = deque([(*START, 0)]) # state i, j, steps
# garden_plots = {START}
# visited = {START}

# MAX_STEPS = 1000
# while q:
#     ci, cj, step = q.popleft()

#     if step % 2 == 0:
#         garden_plots.add((ci, cj))

#     if step == MAX_STEPS:
#         continue

#     for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
#         ni, nj = ci + di, cj + dj
#         npi, npj = periodic_boundaries(ni, nj)
#         if (ni, nj) in visited or grid[npi][npj] == "#":
#             continue
#         q.append((ni, nj, step+1))
#         visited.add((ni, nj))

  
# print("Solution Part 2: ", len(garden_plots))

