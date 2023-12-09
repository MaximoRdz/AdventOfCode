
with open("day-5/input.txt", "r") as file:
    almanac = file.read()

seeds, *almanac = almanac.split("\n")
almanac.pop(0)  # first element is ""

# get seed number
_, seeds = seeds.split(":")
seeds = [int(x) for x in seeds.split()]


def has_number(s):
    for c in s:
        if c.isdigit():
            return True
    return False


almanac_map = {}
n = 0 # 0 seeds; 1 seeds to soil; ...
for i, line in enumerate(almanac):
    if line != "":
        if has_number(line):
            destination, source, length = [int(x) for x in line.split()]
            almanac_map[n].append([destination, source, length])
        else:
            almanac_map[n] = []
    else:
        n += 1
            
def in_range(num, start, length):
    return start <= num < start+length

def get_next(num, source=0, destination=0):
    # if num in range then provide source and destination
    # if not use get_next(num) (save this for performance)
    num_ind = num - source
    return destination+num_ind

def seed_to_soil(seed):
    soil_map = almanac_map[1]
    converted = seed
    for soil in soil_map:
        destination, source, length = soil
        if in_range(seed, source, length):
            converted = get_next(seed, source, destination)

    return converted

def seed_to_location(seed):
    previous = seed
    next = seed
    for key, map in almanac_map.items():
        for map_line in map:
            destination, source, length = map_line
            if in_range(previous, source, length):
                next = get_next(previous, source, destination)
        previous = next

    return previous

locations = [seed_to_location(seed) for seed in seeds]

print("Part 1: ", min(locations))

# seed = [start, len, start, len, start, len, ...]
# at least not with my computational power
def find_min_location(seeds):
    min_location = 1e11
    for i in range(0, len(seeds), 2):
        start, n = seeds[i], seeds[i+1]
        for seed in range(start, start+n):
            location = seed_to_location(seed)
            if location < min_location:
                min_location = location
    return min_location
    
print("Part 2: ", find_min_location(seeds))


# seeds: 79 14 55 13
#
# seed-to-soil map:
# 50 98 2
# 52 50 48
#
# first line = 50 98 2         destination range start;   source range start; range len;
# second line = 52 50 48       destination range start;   source range start; range len;
#
# any number not mapped correspond to same destination i.e. 10 -> 10
#
# seed 79 in   [50, 51, ... 97] (source range)
# destination  [52, ...] so 79 in source corresponds to 81-SOIL
#
# pseudo-code 
#
# seed n 
#     if not in source:
#         n seed -> n soil
#     else:
#         seed-to-soil map:
#             destination(n): 
#                 i = position in [source to source+len-1]
#                 return [destination to destination+len-1][i]
# iterate now for soil to fertilizer
            

