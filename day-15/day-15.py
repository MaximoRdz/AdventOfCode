
with open("day-15/input.txt", "r") as file:
    data = file.read().replace("\n", "")




def hash_map(s):
    current = 0
    for c in s:
        current = (current + ord(c))*17  % 256
    return current


ans = 0
for s in data.split(","):
    ans += hash_map(s)
print("solution part 1: ", ans)
