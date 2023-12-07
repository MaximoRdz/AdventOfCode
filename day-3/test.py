

with open("day-3/example.txt", "r") as file:
    lines = file.read().splitlines()

motor_matrix = [[c for c in line] for line in lines]


NROWS = len(motor_matrix)
NCOLS = len(motor_matrix[0])


def is_symbol(elem):
    if elem == "." or elem.isdigit():
        return False
    else:
        return True


ADJACENT_IND = [
    [-1, -1], [-1, 0], [-1, +1], 
    [0, -1], [0, +1], 
    [+1, -1], [+1, 0], [+1, +1]
]

def is_adjacent(i, j):
    adjacent = False
    neighbor_gears = []
    for y, x in ADJACENT_IND:
        if (0 <= i+y < NROWS) and (0 <= j+x < NCOLS):
            neighbor_char = motor_matrix[i+y][j+x]
            
            if is_symbol(neighbor_char):
                adjacent = True
                # gear -> *
                if neighbor_char == "*":
                    neighbor_gears.append([i+y, j+x])

    return adjacent, neighbor_gears




adjacent_list = []

for i in range(NROWS):
    named_int = ""
    gears_number = []
    adjacent = False

    for j in range(NCOLS):
        char = motor_matrix[i][j]

        if char.isdigit():
            # accumulate int
            named_int += char
            

            # check if adjacent
            adjacent_aux, neighbor_gears = is_adjacent(i, j)
            adjacent += adjacent_aux # only one is sufficient

            gears_number.append(neighbor_gears)

            if j == NCOLS-1 and adjacent and named_int:
                # save right border edge case
                adjacent_list.append((int(named_int), gears_number))
        else:
            if named_int and adjacent:
                # if the name accumulation is not empty and is adjacent
                adjacent_list.append((int(named_int), gears_number))
            named_int = ""
            gears_number = []
            adjacent = False
        


print(adjacent_list)
print(sum([number for number, _ in adjacent_list]))

# The missing part wasn't the only issue - one of the gears 
# in the engine is wrong. A gear is any * symbol that is 
# adjacent to exactly two part numbers. Its gear ratio is 
# the result of multiplying those two numbers together.
