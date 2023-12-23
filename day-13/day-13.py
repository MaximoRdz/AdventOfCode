

with open("day-13/input.txt", "r") as file:
    maps = file.read().split("\n\n")

patterns = [map.split("\n") for map in maps]

def vertical_symmetry(row, n, m):
    left = row[n]
    right = row[m]
    return left == right

def check_vertical(row, n, m):
    if n == 0: 
        return vertical_symmetry(row, n, m)
    if m == len(row)-1:
        return vertical_symmetry(row, n, m)
    
    if n>0 and m<len(row):
        if vertical_symmetry(row, n, m):
             return check_vertical(row, n-1, m+1)
        else:
            return False

def horizontal_symmetry(pattern, n, m):
    return pattern[n] == pattern[m]

def check_horizontal(pattern, n, m):
    if n == 0: 
        return horizontal_symmetry(pattern, n, m)
    if m == len(pattern)-1:
        return horizontal_symmetry(pattern, n, m)
    
    if n>0 and m<len(pattern):
        if horizontal_symmetry(pattern, n, m):
             return check_horizontal(pattern, n-1, m+1)
        else:
            return False

def check_pattern(pattern):
    NCOLS = len(pattern[0])
    NROWS = len(pattern)

    result = 0
    # check horizontal
    for i in range(0, NROWS-1):
        horizontal = 0.5+i
        n, m = int(horizontal-0.5), int(horizontal+0.5)
        if check_horizontal(pattern, n, m):
            result += 100*(horizontal+0.5)
    # check vertical
    for i in range(0, NCOLS-1):
        vertical = 0.5+i
        n, m = int(vertical-0.5), int(vertical+0.5)
        if all(map(lambda x: check_vertical(x, n, m), pattern)):
            result += vertical+0.5
    return result

ans = 0
for pattern in patterns:
    ans += check_pattern(pattern)

print("Solution Part 1: ", int(ans))



