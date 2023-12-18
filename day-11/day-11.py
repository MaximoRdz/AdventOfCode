
with open("day-11/input.txt", "r") as file:
    obs = file.read().split("\n")

obs_matrix = [[c for c in row] for row in obs]



def expand_matrix(matrix):
    # if not galaxy in row or column then its duplicated
    rows_ind = []
    for i, line in enumerate(matrix):
        if len(set(line)) == 1:
            rows_ind.append(i)

    cols_ind = []
    for j in range(len(matrix[0])):
        column = [matrix[i][j]  for i in range(len(matrix))]
        if len(set(column)) == 1:
            cols_ind.append(j)

    # insert rows
    row = ["." for _ in range(len(matrix[0]))]
    for n, i in enumerate(rows_ind):
        matrix.insert(i+n, row.copy())

    # # insert cols
    for row in matrix:
        for n, j in enumerate(cols_ind):
            row.insert(j+n, ".")

    return matrix


obs_matrix = expand_matrix(obs_matrix)

def order_galaxies(matrix):
    galaxies = {}
    count = 1
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "#":
                galaxies[count] = (i, j)
                count += 1
    return galaxies, count-1

galaxies, num_gal = order_galaxies(obs_matrix)


def get_distance(gal1, gal2):
    y1, x1 = galaxies[gal1]
    y2, x2 = galaxies[gal2]
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



