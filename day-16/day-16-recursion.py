

with open("day-16/input.txt", "r") as file:
    matrix = file.read().split("\n")


grid = [[s for s in row] for row in matrix]
NROWS = len(grid)
NCOLS = len(grid[0])
visited = [[" " for j in range(NCOLS)] for i in range(NROWS)]

# print(*grid, sep="\n")

# Beam initial coordinates (i, j)
# Beam direction
#   - row left (0, -1)
#   - row right (0, 1)
#   - column up (-1, 0)
#   - column down (1, 0)

cache = set()
def beam_ray(beam_i, beam_j, dir_i, dir_j):
    key = (beam_i, beam_j, dir_i, dir_j)
    if key in cache:
        return None
    
    cache.add(key)

    next_i, next_j = beam_i+dir_i, beam_j+dir_j
    if not (0<=next_i<NROWS and 0<=next_j<NCOLS):
        return None
    
    visited[next_i][next_j] = "#"
    next_tile = grid[next_i][next_j]

    if next_tile == ".":
        aux = beam_ray(next_i, next_j, dir_i, dir_j)
    elif next_tile == "-":
        if dir_i == 0:
            aux = beam_ray(next_i, next_j, dir_i, dir_j)
        else:
            aux = beam_ray(next_i, next_j, 0, 1)
            aux = beam_ray(next_i, next_j, 0, -1)
    elif next_tile == "|":
        if dir_i == 0:
            aux = beam_ray(next_i, next_j, 1, 0)
            aux = beam_ray(next_i, next_j, -1, 0)
        else:
            aux = beam_ray(next_i, next_j, dir_i, dir_j)
    elif next_tile == "\\":
        aux = beam_ray(next_i, next_j, dir_j, dir_i)
    elif next_tile == "/":
        aux = beam_ray(next_i, next_j, -dir_j, -dir_i)
    else:
        return None
    
    return None

def visited_tiles(visited):
    ans = 0
    for row in visited:
        for col in row:
            ans += 0 if col==" " else 1
    return ans

visited[0][0] = "#"
# beam_ray(0, 0, 0, 1)
# print("Solution Part 1: ", visited_tiles(visited))

beam_ray(0, 0, 1, 0)
print("Solution Part 1: ", visited_tiles(visited))
# print(cache)
# print(*visited, sep="\n")


    







    