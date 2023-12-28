from collections import deque


with open("day-16/input.txt", "r") as file:
    matrix = file.read().split("\n")

grid = [[s for s in row] for row in matrix]
NROWS = len(grid)
NCOLS = len(grid[0])

# Beam initial coordinates (i, j)
# Beam direction
#   - row left (0, -1)
#   - row right (0, 1)
#   - column up (-1, 0)
#   - column down (1, 0)

beam_i, beam_j = 0, 0
dir_i, dir_j = 1, 0

visited = set()
visited.add((beam_i, beam_j))

cache = set()
tile_queue = deque()
tile_queue.append((beam_i, beam_j, dir_i, dir_j))

while len(tile_queue):
    beam_i, beam_j, dir_i, dir_j = tile_queue.popleft()
    key = (beam_i, beam_j, dir_i, dir_j)
    if key in cache:
        continue
    cache.add(key)

    next_i, next_j = beam_i+dir_i, beam_j+dir_j
    if not (0<=next_i<NROWS and 0<=next_j<NCOLS):
        continue

    visited.add((next_i, next_j))
    next_tile = grid[next_i][next_j]

    if next_tile == ".":
        tile_queue.append((next_i, next_j, dir_i, dir_j))
    elif next_tile == "-":
        if dir_i == 0:
            tile_queue.append((next_i, next_j, dir_i, dir_j))
        else:
            tile_queue.append((next_i, next_j, 0, 1))
            tile_queue.append((next_i, next_j, 0, -1))
    elif next_tile == "|":
        if dir_i == 0:
            tile_queue.append((next_i, next_j, 1, 0))
            tile_queue.append((next_i, next_j, -1, 0))
        else:
            tile_queue.append((next_i, next_j, dir_i, dir_j))
    elif next_tile == "\\":
        tile_queue.append((next_i, next_j, dir_j, dir_i))
    elif next_tile == "/":
        tile_queue.append((next_i, next_j, -dir_j, -dir_i))
    else:
        continue

print("Solution Part 1: ", len(visited))
    
