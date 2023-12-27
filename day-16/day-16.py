

with open("day-16/example.txt", "r") as file:
    matrix = file.read().split("\n")


grid = [[s for s in row] for row in matrix]
NROWS = len(grid)
NCOLS = len(grid[0])
visited = [[False for j in range(NCOLS)] for i in range(NROWS)]

print(*grid, sep="\n")

# Beam initial coordinates (i, j)
# Beam direction
#   - row left (0, -1)
#   - row right (0, 1)
#   - column up (-1, 0)
#   - column down (1, 0)

def beam_ray(beam_i, beam_j, dir_i, dir_j):
    next_i, next_j = beam_i+dir_i, beam_j+dir_j
    if not (0<=next_i<NROWS and 0<=next_j<NCOLS):
        return None
    
    visited[next_i][next_j] = True
    next_tile = grid[next_i][next_j]

    if next_tile == ".":
        beam_ray(next_i, next_j, dir_i, dir_j)
    elif next_tile == "-":
        if dir_i == 0:
            beam_ray(next_i, next_j, dir_i, dir_j)
        else:
            beam_ray(next_i, next_j, 0, 1)
            beam_ray(next_i, next_j, 0, -1)
    elif next_tile == "|":
        if dir_i == 0:
            beam_ray(next_i, next_j, 1, 0)
            beam_ray(next_i, next_j, -1, 0)
        else:
            beam_ray(next_i, next_j, dir_i, dir_j)
    elif next_tile == "\\":
        pass
    elif next_tile == "/":
        pass
    else:
        return None

    
    







    