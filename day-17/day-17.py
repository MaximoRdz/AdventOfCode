


with open("day-17/example.txt", "r") as file:
    data = file.read().split("\n")

grid = [[int(s) for s in row] for row in data]

# print(*grid, sep="\n")

# direction convention:
# go row right = (0, 1)
# go row left = (0, -1)
# go column down = (1, 0)
# go column up = (-1, 0)
def path_cost(i0, j0, dir_i, dir_j):
    pass
