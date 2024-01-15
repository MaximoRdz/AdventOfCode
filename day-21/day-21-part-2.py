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
print("One size excluding I, J = 0, 0: ", MAX_STEPS//N)
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
# top, bottom, left and right corners
# partially filled diagonal grids
# inner grids: 
#     * 
# odd: 1, 8, 16 , 24, 46

even = reach(*START, 2*N)
odd = reach(*START, 2*N+1)

even_sum = 0
odd_sum = 0
# perimeter p(s) = 4*s
for s in range(1, int(MAX_STEPS//N + 1)): 
    if s % 2 == 0:
        odd_sum += 4*s
    else:
        even_sum += 4*s
odd += 1

print("Allowed states with even steps: ", even, "Total Sum of reachable states: ", even_sum)
print("Allowed states with odd steps:  ", odd, "Total Sum of reachable states: ", odd_sum)

# corner edge cases
top_corner = reach(NROWS-1, START[1], N-1) # N steps left
bottom_corner = reach(0, START[1], N-1) 
right_corner = reach(START[0], 0, N-1) 
left_corner = reach(START[0], NCOLS-1, N-1) 

# partially fill surrounding diagonals
outer_first = reach(NROWS-1, 0, N//2 - 1)
outer_second = reach(NROWS-1, NCOLS-1, N//2 - 1)
outer_third = reach(0, NCOLS-1, N//2 - 1)
outer_fourth = reach(0, 0, N//2 - 1)

inner_first = reach(NROWS-1, 0, 3*N//2 - 1)
inner_second = reach(NROWS-1, NCOLS-1, 3*N//2 - 1)
inner_third = reach(0, NCOLS-1, 3*N//2 - 1)
inner_fourth = reach(0, 0, 3*N//2 - 1)

print("Solution Part 2: Sum of all the reachable states: ",
      even_sum*even + odd_sum*odd + 
      top_corner + bottom_corner + right_corner + left_corner +
      (MAX_STEPS//N) * (outer_first + outer_second + outer_third + outer_fourth) + 
      (MAX_STEPS//N - 1) * (inner_first + inner_second + inner_third + inner_fourth)
    )

# 1404650519355872 too high
# 592770703036352
# 592770703043579
#



