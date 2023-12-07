import re

# is_symbol(): if is not number nor period then it is a symbol
# is_adjacent()


with open("day-3/example.txt", "r") as file:
    lines = file.read().splitlines()
    
nrows = len(lines)
ncols = len(lines[0])


def is_symbol(elem):
    if elem == ".":
        return False
    elif elem.isdigit():
        return False
    else:
        return True


def is_adjacent(number, line_ind):
    n1, n2 = re.search(str(number), lines[line_ind]).span()
    for number_ind in [n1, n2-1]:
        # digit coordinates i,j = line_ind, number_ind
        # if there is top line and it is not corner
        if (line_ind != 0) and (number_ind != 0) and (number_ind != ncols-1):
            # check top
            if is_symbol(lines[line_ind-1][number_ind]):
                return True
            # check t-l corner 
            if is_symbol(lines[line_ind-1][number_ind-1]):
                return True
            # check t-r corner
            if is_symbol(lines[line_ind-1][number_ind+1]):
                return True
        # if there is bottom line and it is not corner
        if (line_ind != nrows-1) and (number_ind != 0) and (number_ind != ncols-1):
            # check bottom
            if is_symbol(lines[line_ind+1][number_ind]):
                return True
            # check b-l corner
            if is_symbol(lines[line_ind+1][number_ind-1]):
                return True
            # check b-r corner
            if is_symbol(lines[line_ind+1][number_ind+1]):
                return True
        # if not first line element
        if number_ind != 0: 
            # check left
            if is_symbol(lines[line_ind][number_ind-1]):
                return True
        # if not last line element
        if number_ind != ncols-1:    
            # check right
            if is_symbol(lines[line_ind][number_ind+1]):
                return True
    return False

adjacent_numbers = []
for line_ind, line in enumerate(lines):
    numbers = re.findall("\d+", line)
    for number in numbers:
        if is_adjacent(number, line_ind):
            adjacent_numbers.append(int(number))
        else:
            continue




print("Part 1: ", sum(adjacent_numbers))
print(adjacent_numbers)




# def is_adjacent(number, line_ind):
#     n1, n2 = re.search(str(number), lines[line_ind]).span()
#     for number_ind in range(n1, n2):
#         # digit coordinates i,j = line_ind, number_ind
#         # top group ---------------------------------------------
#         if line_ind == 0:
#             # top left corner
#             if number_ind == 0:
#                 if is_symbol(lines[line_ind][number_ind+1]):
#                     return True
#                 elif is_symbol(lines[line_ind+1][number_ind+1]):
#                     return True
#                 elif is_symbol(lines[line_ind+1][number_ind]):
#                     return True
#                 else:
#                     continue
#             # top right corner
#             elif number_ind == ncols-1:
#                 if is_symbol(lines[line_ind][number_ind-1]):
#                     return True
#                 elif is_symbol(lines[line_ind-1][number_ind-1]):
#                     return True
#                 elif is_symbol(lines[line_ind+1][number_ind]):
#                     return True
#                 else:
#                     continue
#             # middle
#             else:
#                 if is_symbol(lines[line_ind][number_ind-1]):
#                     return True
#                 elif is_symbol(lines[line_ind][number_ind+1]):
#                     return True
#                 elif is_symbol(lines[line_ind+1][number_ind]):
#                     return True
#                 else:
#                     continue

#         # bottom group ---------------------------------------------
#         elif line_ind == nrows-1:
#             # bottom left corner
#             if number_ind == 0:
#                 if is_symbol(lines[line_ind][number_ind+1]):
#                     return True
#                 elif is_symbol(lines[line_ind-1][number_ind+1]):
#                     return True
#                 elif is_symbol(lines[line_ind-1][number_ind]):
#                     return True
#                 else:
#                     continue
#             # bottom right corner
#             elif number_ind == ncols-1:
#                 if is_symbol(lines[line_ind][number_ind-1]):
#                     return True
#                 elif is_symbol(lines[line_ind-1][number_ind-1]):
#                     return True
#                 elif is_symbol(lines[line_ind-1][number_ind]):
#                     return True
#                 else:
#                     continue
#             # middle
#             else:
#                 if is_symbol(lines[line_ind][number_ind-1]):
#                     return True
#                 elif is_symbol(lines[line_ind][number_ind+1]):
#                     return True
#                 elif is_symbol(lines[line_ind-1][number_ind]):
#                     return True
#                 else:
#                     continue
#         # left side group ----------------------------------------------------
#         elif (number_ind == 0) and (line_ind != 0) and (line_ind != nrows-1):
#             if is_symbol(lines[line_ind-1][number_ind]):
#                 return True
#             elif is_symbol(lines[line_ind][number_ind+1]):
#                 return True
#             elif is_symbol(lines[line_ind+1][number_ind]):
#                 return True
#             else:
#                 continue
#         # right side group ----------------------------------------------------
#         elif (number_ind == ncols-1) and (line_ind != 0) and (line_ind != nrows-1):
#             if is_symbol(lines[line_ind-1][number_ind]):
#                 return True
#             elif is_symbol(lines[line_ind][number_ind-1]):
#                 return True
#             elif is_symbol(lines[line_ind+1][number_ind]):
#                 return True
#             else:
#                 continue
#         # center of the matrix
#         else:
#             if is_symbol(lines[line_ind-1][number_ind]):
#                 return True
#             elif is_symbol(lines[line_ind-1][number_ind+1]):
#                 return True
#             elif is_symbol(lines[line_ind-1][number_ind-1]):
#                 return True
#             elif is_symbol(lines[line_ind][number_ind+1]):
#                 return True
#             elif is_symbol(lines[line_ind][number_ind-1]):
#                 return True
#             elif is_symbol(lines[line_ind+1][number_ind]):
#                 return True
#             elif is_symbol(lines[line_ind+1][number_ind+1]):
#                 return True
#             elif is_symbol(lines[line_ind+1][number_ind-1]):
#                 return True
#     return False