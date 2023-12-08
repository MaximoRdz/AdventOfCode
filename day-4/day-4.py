import re 


scracth_cards = {}
with open("day-4/example.txt", "r") as file:
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

print(ans)

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
print(total_card_num)
# def winning_recursion(card_ind):
#     # card_ind: card 1 example
#     # card_num: matching numbers card 1 -> 4
#     card_ind_int = int(re.findall("\d+", card_ind)) # i.e. 1
#     card_num = scracth_cards[card_ind][2]
#     for copy_ind_int in range(card_ind_int+1, card_ind_int+card_num+1):
#                             # 2,            1+4+1=5     -> 2, 3, 4, 5
#         copy_card_ind = f"Card {copy_ind_int}"  # i.e. Card 2
#         copy_card_num = scracth_cards[copy_card_ind][2] # i.e. 2
#         return winning_recursion(copy_card_ind)

# winning_recursion("Card 1", 3)
