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
    result = match_lists(value[0], value[1])
    scracth_cards[key].append(result)
    ans += card_value(result)

print("Solution Part 1: ", ans)

# problem 1: careful with how you split string if you keep "" values
# you'll way more matches than the reality
#
# problem 2: duplicate values on the elf list is not an issue proof: 
#         for elem in last_list:
#             if last_list.count(elem) > 1:
#                 print(key, ", ", elem, ", ",  last_list.count(elem))

# Part 2 ------------------------------------
# Right now the dict looks
# {'Card 1': [['41', '48', '83', '86', '17'], 
# ['83', '86', '6', '31', '17', '9', '48', '53'], 4], ...
# so we know the index and the winning numbers of each card

total_card_num = dict.fromkeys(scracth_cards.keys())
# Initialized dict
for key in total_card_num.keys():
    total_card_num[key] = 0


# card 1 children
def get_key(child_int):
    n = 4 - len(str(child_int))
    key = "Card" + n*" " + str(child_int)
    return key

def get_children(card_ind):
    card_int = int(re.findall("\d+", card_ind)[0])
    num_children = scracth_cards[card_ind][2]
    children = [get_key(child) for child in range(card_int+1, 
                                                   card_int+num_children+1)]
    return children


def save_children_copy(children):
    for child in children:
        total_card_num[child] += 1


def check_children(children):
    """
    Recursive solution of the problem (not best run time)
    """
    if not children:
        # check is not empty
        return 0
    else:
        # print(children)
        save_children_copy(children)
        aux = []
        for child in children:
            aux.extend(get_children(child))
        return check_children(aux)

a = check_children(list(total_card_num.keys()))
# print("Recursive prizes: ", total_card_num)
print("Solution Part 2: ", sum(list(total_card_num.values())))
