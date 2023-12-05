# # Rules
# 12 red cubes
# 13 green cubes
# 14 blue cubes
# 39 total

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14
MAX_TOTAL = MAX_GREEN + MAX_RED + MAX_BLUE

def is_valid_set(blue=0, red=0, green=0):
    if (blue > MAX_BLUE) or (red > MAX_RED) or (green > MAX_GREEN) or ((blue+red+green) > MAX_TOTAL):
        return False
    else: 
        return True


def get_cube_colors(set_cubes):
    # set_cubes = ["3blue", "4red"]
    red, blue, green = 0, 0, 0
    for color_set in set_cubes:
        if "blue" in color_set:
            blue = int(color_set.removesuffix("blue"))
        elif "red" in color_set:
            red = int(color_set.removesuffix("red"))
        elif "green" in color_set:
            green = int(color_set.removesuffix("green"))
        else: 
            print("This should never be reached")
    return blue, red, green


def is_valid_game(game):
    # Game=" 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n"
    game.replace(" ", "")
    game_sets = game.split(";")

    for game_set in game_sets:
        set_cubes = game_set.split(",")
        blue, red, green = get_cube_colors(set_cubes)
        if not is_valid_set(blue, red, green):
            return False
        else:
            continue
    
    return True


def game_id(game_id_str):
    return int(game_id_str.split(" ")[1])

with open("./input.txt", "r") as myfile:
    lines = myfile.readlines()

    sum_game_id = 0
    for line in myfile.readlines():
        line = line.replace("\n", "")
        game_id_str, game = line.split(":")
            
        if is_valid_game(game):
            sum_game_id += game_id(game_id_str)
        else: 
            continue

print(sum_game_id)