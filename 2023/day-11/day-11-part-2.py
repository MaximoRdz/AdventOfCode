

with open("day-11/input.txt", "r") as file:
    obs = file.read().split("\n")


def get_expand_info(matrix):
    rows_ind = []
    for i, line in enumerate(matrix):
        if len(set(line)) == 1:
            rows_ind.append(i)

    cols_ind = []
    for j in range(len(matrix[0])):
        column = [matrix[i][j]  for i in range(len(matrix))]
        if len(set(column)) == 1:
            cols_ind.append(j)
    return rows_ind, cols_ind

rows_ind, cols_ind = get_expand_info(obs)

def real_coords(y, x, EXPANSION_FACTOR = int(1e6)):
    # EXPANSION_FACTOR: replace 1 value to exp_factor as many values
    scale_x = len(list(filter(lambda j: j<x, cols_ind)))
    scale_y = len(list(filter(lambda i: i<y, rows_ind)))
    return scale_y*(EXPANSION_FACTOR-1) + y, scale_x*(EXPANSION_FACTOR-1) + x


def order_galaxies(matrix):
    # not expanded grid
    galaxies = {}
    count = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                galaxies[count] = (i, j)
                count += 1
    return galaxies, count-1

galaxies, num_gal = order_galaxies(obs)


def get_distance(gal1, gal2):
    y1, x1 = galaxies[gal1]
    y1, x1 = real_coords(y1, x1)
    y2, x2 = galaxies[gal2]
    y2, x2 = real_coords(y2, x2)

    if x1 == x2: 
        # vertically aligned
        return abs(y2-y1)
    elif y1 == y2: 
        # horizontally aligned
        return abs(x2-x1)
    else:
        return abs(y2-y1) + abs(x2-x1)


pair_distances = []

for i in range(1, num_gal):
    for j in range(i+1, num_gal+1):
        pair_distances.append(get_distance(i,j))

print("Solution Part 1: ", sum(pair_distances))