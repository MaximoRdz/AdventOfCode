import os

# -----------------------------------------------------------------------------------------------
# PART 1
# -----------------------------------------------------------------------------------------------

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

# -----------------------------------------------------------------------------------------------
# PART 2
# -----------------------------------------------------------------------------------------------


numbers_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "zero"]
numbers_int = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
numbers = dict(zip(numbers_str, numbers_int))

# string method find() returns the lowest index where sub is found and -1 if it is not found
# string method rfind() returns the highest index ...
# Idea: 
# >>> list(map(str.isdigit, "a4hnj4j234")) 
# [False, True, False, False, False, True, False, True, True, True]
# get first and last True index
def get_calibration_value_b(line):
    digit_values = list(map(str.isdigit, line))
    first_digit_index = digit_values.index(True)
    first_digit_number = line[first_digit_index]  # str

    digit_values.reverse()
    last_digit_index = (len(digit_values)-1) - digit_values.index(True)
    last_digit_number = line[last_digit_index]  # str

    # last_str_number and its index
    # first_str_number and its index
    # last_digit_number and its index
    # first_digit_number and its index
    
    final_candidates = {first_digit_index: first_digit_number,   #  notice that dict removes duplicate 
                        last_digit_index: last_digit_number}     # so i'm using unique indexes instead

    number_positions = {}
    for number in numbers_str:
        first_num_index = line.find(number)
        last_num_index = line.rfind(number)
        if first_num_index != -1:
            # sub string present on the line
            number_positions[number] = [first_num_index, last_num_index] # [0, 5] or [3, 3] if equal
        else:
            continue

    save_min = 100 # ensure first true
    save_max = -1 # ensure first true
    if number_positions:
        # not empty dict
        # look for the smallest index and associated number_str
        for key, value_list in number_positions.items():
            first_str_ind = min(value_list)
            last_str_ind = max(value_list)
            if first_str_ind < save_min:
                save_min = first_str_ind
                first_str_number = numbers[key]
                final_candidates[save_min] = first_str_number
            if last_str_ind > save_max:
                save_max = last_str_ind
                last_str_number = numbers[key]
                final_candidates[save_max] = last_str_number


    calibration_list = list(sorted(final_candidates.items(), key=lambda values_tuple: values_tuple[0]))
    calibration_value_first = calibration_list[0][1]
    calibration_value_last = calibration_list[-1][1]

    return int("".join([calibration_value_first, calibration_value_last]))


print("Solution Part 2: ", sum(map(get_calibration_value_b, lines)))



# # test: 

# with open("day-1/test.txt", "r") as file:
#     for line in file.readlines():
#         print(line.replace("\n", ""), ":\t", get_calibration_value_b(line))

# # code is failing 
# #     - when the line starts with a str numbers
# #     - when it ends with a digit number

# # failing examples
# # eight691seven8cxdbveightzv :     68
# # prcnjkshkvlcgsixfiveone6 :       61

# line_test_1 = "eight691seven8cxdbveightzv"
# line_test_2 = "prcnjkshkvlcgsixfiveone6"

# print("Test 1: ", line_test_1, "\t", get_calibration_value_b(line_test_1))
# print("Test 2: ", line_test_2, "\t", get_calibration_value_b(line_test_2))

