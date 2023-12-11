from collections import defaultdict


# joker rule J
# following part 1 model we only need to modify 
# the get_play_name function

with open("day-7/input.txt", "r") as file:
    game = file.read().split("\n")

# hands = [play.split()[0] for play in game]
# bids = [play.split()[1] for play in game]

plays = {play.split()[0]: int(play.split()[1]) for play in game}


play_names = ("five", "four", "full", "three", "two-pair", "one-pair", "high")
play_values = (25, 17, 13, 11, 9, 7, 5)
play_value_name = dict(zip(play_values, play_names))
play_name_value = dict(zip(play_names, play_values))


def joker_hand(play):
    """ 
    given a play that contains a joker return 
    the best possible hand it could be played
    changing J for that card
    """
    # KT JJ T -> KT TT T
    # the best possible play is changing J to 
    # the card with more occurences
    max_ocur = 0
    new_card = "J"
    for c in play:
        if c == "J":
            continue
        if max_ocur < play.count(c):
            max_ocur = play.count(c)
            new_card = c 
    # print("prev: ", play, "new: ", play.replace("J", new_card))
    if new_card == "J":
        # edge case all j's
        new_card == "A"
    play = play.replace("J", new_card)

    return play


def get_play_name(play):
    """
    five: 5*5 = 25
    four: 4*4 + 1 = 17
    full: 3*3 + 2*2 = 13
    three: 3*3 + 1*1 + 1*1 = 11
    two-pair: 2*2 + 2*2 + 1 = 9
    one-pair: 2*2 + 3*1 = 7
    high: 5*1 = 5
    """
    if "J" in play:
        play = joker_hand(play)
    ans = 0
    for c in play:
        ans += play.count(c)
    return play_value_name[ans]

# classify per play name
play_classify = defaultdict(list)
for play in plays.keys():
    play_classify[get_play_name(play)].append(play)


# order categories by card strength
card_name = ("A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J")
card_value = (13, 12, 11, 10, 9, 8, 7, 6, 5, 4 ,3, 2, 1)
card_name_value = dict(zip(card_name, card_value))

def is_new_larger(new, cur):
    for new_c, cur_c in zip(new, cur):
        if card_name_value[new_c] == card_name_value[cur_c]:
            continue
        elif card_name_value[new_c] > card_name_value[cur_c]:
            return True
        else:
            return False


def order_category(play_list):
    for i in range(1, len(play_list)):
        for j in range(0, i):
            if is_new_larger(play_list[i], play_list[j]):
                play_list[i], play_list[j] = play_list[j], play_list[i]
    return play_list


order_plays = []
for key, value in sorted(play_classify.items(), key=lambda elem: play_name_value[elem[0]], reverse=True):
    order_plays.extend(order_category(value))

N = len(order_plays)
ans = 0
for i, play in enumerate(order_plays):
    ans += (N-i) * plays[play]

print("solution part 2: ", ans)