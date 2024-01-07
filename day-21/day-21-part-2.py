from collections import deque, defaultdict

with open("day-21/example.txt", "r") as file:
    data = file.read().splitlines()


grid = []
for i, line in enumerate(data):
    grid.append([])
    for j, c in enumerate(line):
        grid[i].append(c)
        if c == "S":
            START = (i, j)

NROWS, NCOLS = len(grid), len(grid[0])

def periodic_boundaries(i, j):
    # a // b = 0 a<b
    # a // b = 1 b<=a<2b
    # . . . 
    ni = i - (i//NROWS)*NROWS
    nj = j - (j//NCOLS)*NCOLS
    return ni, nj 

q = deque([(*START, 0)]) # state i, j, steps
garden_plots = {START}
visited = {START}

MAX_STEPS = 1000
while q:
    ci, cj, step = q.popleft()

    if step % 2 == 0:
        garden_plots.add((ci, cj))

    if step == MAX_STEPS:
        continue

    for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        ni, nj = ci + di, cj + dj
        npi, npj = periodic_boundaries(ni, nj)
        if (ni, nj) in visited or grid[npi][npj] == "#":
            continue
        q.append((ni, nj, step+1))
        visited.add((ni, nj))

  
print("Solution Part 2: ", len(garden_plots))

