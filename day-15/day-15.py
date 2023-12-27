from collections import defaultdict


with open("day-15/input.txt", "r") as file:
    data = file.read().replace("\n", "")


sequence = defaultdict(list)

def hash_map(s):
    current = 0
    for c in s:
        current = (current + ord(c))*17  % 256
    return current

def split_data(s):
    if "-" in s:
        return "-", s.split("-")[0]
    else:
        return "=", s.split("=")

def dash_operation(label):
    box = hash_map(label)
    for i, lens in enumerate(sequence[box]):
        if label in lens:
            sequence[box].pop(i)
            break


def equal_operation(label, lens_value):
    box = hash_map(label)
    for i, lens in enumerate(sequence[box]):
        if label in lens:
            sequence[box].pop(i)
            sequence[box].insert(i, [label, lens_value])
            break
    else:
        sequence[box].append([label, lens_value])
    

def focusing_power():
    result = 0
    for box, lenses in sequence.items():
        if lenses:
            for i, lens in enumerate(lenses):
                result += (int(box)+1) * (i+1) * int(lens[1])
    return result

# ans = 0
# for s in data.split(","):
#     ans += hash_map(s)
# print("solution part 1: ", ans)
        
for i, s in enumerate(data.split(",")):
    operation, item_data = split_data(s)
    if operation == "-":
        dash_operation(item_data)
    else:
        equal_operation(*item_data)

print("Solution Part 2: ", focusing_power())
