from collections import deque


with open("day-16/input.txt", "r") as file:
    matrix = file.read().split("\n")

grid = [[s for s in row] for row in matrix]
NROWS = len(grid)
NCOLS = len(grid[0])

def beam_energized_tiles(beam_i, beam_j, dir_i, dir_j):
    visited = set()
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
        
    return len(visited)

# Beam initial coordinates (i, j)
# Beam direction
#   - row left (0, -1)
#   - row right (0, 1)
#   - column up (-1, 0)
#   - column down (1, 0)

# fixed bug initial tile is not ".": 
# Added extra dot value arrays surrounding the matrix
initial_shoots = []
initial_shoots.extend([(-1, j, 1, 0) for j in range(NCOLS)])
initial_shoots.extend([(NROWS, j, -1, 0) for j in range(NCOLS)])
initial_shoots.extend([(i, -1, 0, 1) for i in range(NROWS)])
initial_shoots.extend([(i, NCOLS, 0, -1) for i in range(NROWS)])

max_tiles = 0
for beam_i, beam_j, dir_i, dir_j in initial_shoots:
    energized_tiles = beam_energized_tiles(beam_i, beam_j, dir_i, dir_j)
    max_tiles = max(max_tiles, energized_tiles)

print("Solution Part 2: ", max_tiles)

    
