

with open("day-3/input.txt", "r") as file:
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
                    neighbor_gears.append((i+y, j+x))

    return adjacent, neighbor_gears




adjacent_list = []
adjacent_number_gears = []

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
                adjacent_list.append(int(named_int))
                adjacent_number_gears.append(gears_number)
        else:
            if named_int and adjacent:
                # if the name accumulation is not empty and is adjacent
                adjacent_list.append(int(named_int))
                adjacent_number_gears.append(gears_number)
            named_int = ""
            gears_number = []
            adjacent = False
        
print("Solution Part 1: ", sum(adjacent_list))

def unpack_list(number_gears):
    unpacked = []
    for item in number_gears:
        if isinstance(item, list):
            unpacked.extend(item)
        elif isinstance(item, tuple):
            unpacked.append(item)
    return unpacked


# create dictionary with gears and associated numbers
gears_dict = {}
for i, number_gears in enumerate(adjacent_number_gears):
    unpack_number_gears = unpack_list(number_gears)
    if unpack_number_gears: # not empty
        for key in list(dict.fromkeys(unpack_number_gears)):
            if key in gears_dict:
                gears_dict[key].append(adjacent_list[i])
            else:
                gears_dict[key] = [adjacent_list[i]]
        
def gear_ratios_sum(gears_dict):
    ans = 0
    for key, value in gears_dict.items():
        if len(value) == 2:
            ans += value[0] * value[1]
    return ans

print("Solution Part 2: ", gear_ratios_sum(gears_dict))


# The missing part wasn't the only issue - one of the gears 
# in the engine is wrong. A gear is any * symbol that is 
# adjacent to exactly two part numbers. Its gear ratio is 
# the result of multiplying those two numbers together.
