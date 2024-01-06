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


MAX_STEPS = 64
q = deque([(*START, 0)]) # state i, j, steps
garden_plots = {START}
visited = {START}

while q:
    ci, cj, step = q.popleft()

    if step % 2 == 0:
        garden_plots.add((ci, cj))

    if step == MAX_STEPS:
        continue

    for di, dj in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        ni = ci + di
        nj = cj + dj
        if not (0 <= ni < NROWS and 0 <= nj < NCOLS) or grid[ni][nj] == "#":
            continue
        if (ni, nj) in visited:
            continue
        q.append((ni, nj, step+1))
        visited.add((ni, nj))
  



print("Solution Part 1: ", len(garden_plots))


