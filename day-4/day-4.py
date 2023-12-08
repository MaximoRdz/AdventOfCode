import re 


scracth_cards = {}
with open("day-4/input.txt", "r") as file:
    for line in file.readlines():
        key, value = line.split(":")
        first_list, last_list = value.split("|")
        first_list, last_list = re.findall("\d+", first_list), re.findall("\d+", last_list)
        scracth_cards[key] = [first_list, last_list]


def match_lists(winning_list, elf_list):
    result = 0
    for win_num in winning_list:
        if win_num in elf_list:
            result += 1
    return result


def card_value(matching_numbers):
    if matching_numbers:
        return 2**(matching_numbers-1)
    else:
        return 0
    

ans = 0
for key, value in scracth_cards.items():
    ans += card_value(match_lists(value[0], value[1]))

print(ans)

# problem 1: careful with how you split string if you keep "" values
# you'll way more matches than the reality
#
# duplicate values on the elf list is not an issue proof: 
#         for elem in last_list:
#             if last_list.count(elem) > 1:
#                 print(key, ", ", elem, ", ",  last_list.count(elem))
