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
    q = deque([(i0, j0, 0)]) # state: i, j, steps
    garden_plots = {(i0, j0)}
    reached = set()

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

print("Start Square: ", START)
even = reach(*START, 2*N)
print("Allowed states with even steps: ", even)
odd = reach(*START, 1)
print("Allowed states with odd steps: ", odd)

"""I'm missing something even and odd scenarios must be different..."""

