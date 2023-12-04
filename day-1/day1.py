import os

# list with every row of the txt input file
with open("day-1/input.txt", "r") as file:
    lines = file.readlines()


def get_calibration_value(line):
    """
    If the list contains more than 2 elements it obvious it works
    and if it contains only one since index 0 and -1 both point to first element 
    it works nicely aswell
    """
    filtered_list = list(filter(str.isdigit, line))
    return int("".join([filtered_list[0], filtered_list[-1]]))
    

print("Solution Part 1: ", sum(map(get_calibration_value, lines)))

numbers_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
numbers_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
numbers = dict(zip(numbers_str, numbers_int))



# string method find() returns the lowest index where sub is found and -1 if it is not found
# string method rfind() returns the highest index ...
# Idea: 
# >>> list(map(str.isdigit, "a4hnj4j234")) 
# [False, True, False, False, False, True, False, True, True, True]
# get first and last True index
line = "a4hnone"
digit_values = list(map(str.isdigit, line))
first_digit_index = digit_values.index(True)

digit_values.reverse()
last_digit_index = (len(digit_values)-1) - digit_values.index(True)

number_positions = {}
for number in numbers_str:
    first_num_index = line.find(number)
    last_num_index = line.rfind(number)
    if first_num_index != -1:
        # sub string present on the line
        number_positions[number] = [first_num_index, last_num_index] # [0, 5] or [3, 3] if equal
    else:
        continue

if number_positions:
    # not empty dict

    # TDOOOOOOOOO
    pass

# I want to keep the two lowest indexes
ind1, ind2 = [first_digit_index, last_digit_index, first_num_index, last_num_index].sort()[:2]

calibration_value_b = int("".join([line[ind1], line[ind2]]))

