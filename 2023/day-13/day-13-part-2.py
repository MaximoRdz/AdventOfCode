

with open("day-13/example.txt", "r") as file:
    maps = file.read().split("\n\n")

patterns = [map.split("\n") for map in maps]


def horizontal_symmetry(pattern, n, m):
    result = 0
    for a, b in zip(pattern[n], pattern[m]):
        result += a!=b
    return result


def check_horizontal(pattern, n, m, smudge_found):

    if n == 0 and horizontal_symmetry(pattern, n, m) == 0 and smudge_found:
        return True
    if m == len(pattern)-1 and horizontal_symmetry(pattern, n, m) == 0 and smudge_found:
        return True
    
    if n == 0 and horizontal_symmetry(pattern, n, m) == 1:
        # only one different
        n_pattern = pattern.copy()
        n_pattern[m] = n_pattern[n]
        return check_horizontal(n_pattern, n, m, True)
    
    if m == len(pattern)-1 and horizontal_symmetry(pattern, n, m) == 1:
        # only one different
        m_pattern = pattern.copy()
        m_pattern[m] = m_pattern[n]
        return check_horizontal(m_pattern, n, m, True)
    
    if n>0 and m<len(pattern)-1:
        if horizontal_symmetry(pattern, n, m) == 0:
            # all the same
            return check_horizontal(pattern, n-1, m+1, False)
        if horizontal_symmetry(pattern, n, m) == 1:
            # only one different
            new_pattern = pattern.copy()
            new_pattern[m] = new_pattern[n]
            return check_horizontal(new_pattern, n-1, m+1, True)

    # return False
    
def vertical_symmetry(row, n, m):
    result = 0
    for a, b in zip(reversed(row[:n+1]), row[m:]):
        result += a!=b
    return result

def check_vertical(row, n, m, smudge_found):
    if n == 0 and vertical_symmetry(row, n, m) == 0 and smudge_found: 
        return True
    if m == len(row)-1 and vertical_symmetry(row, n, m) == 0 and smudge_found:
        return True

    if n == 0 and vertical_symmetry(row, n, m) == 1: 
        n_row = row[:n] + row[m] + row[n+1:m] + row[m:]
        return check_vertical(n_row, n, m, True)
    if m == len(row)-1 and vertical_symmetry(row, n, m) == 1:
        m_row = row[:n] + row[m] + row[n+1:m] + row[m:]
        return check_vertical(m_row, n, m, True)

    if n>0 and m<len(row)-1:
        if vertical_symmetry(row, n, m) == 0:
             return check_vertical(row, n-1, m+1, False)
        if vertical_symmetry(row, n, m) == 1:
            new_row = row[:n] + row[m] + row[n+1:m] + row[m:]
            return check_vertical(new_row, n-1, m+1, True)

def check_pattern(pattern):
    NCOLS = len(pattern[0])
    NROWS = len(pattern)

    result = 0
    # check horizontal
    for i in range(0, NROWS-1):
        horizontal = 0.5+i
        n, m = int(horizontal-0.5), int(horizontal+0.5)

        if check_horizontal(pattern, n, m, False):
            print("\thorizontal sym")
            result += 100*(horizontal+0.5)

    # check vertical
    for i in range(0, NCOLS-1):
        vertical = 0.5+i
        n, m = int(vertical-0.5), int(vertical+0.5)
        if all(map(lambda x: check_vertical(x, n, m, False), pattern)):
            print("\tvertical sym")
            result += vertical+0.5
    

    return result

ans = 0
i = 1
for pattern in patterns:
    print(i, ": ")
    ans += check_pattern(pattern)
    i += 1

print("Solution Part 2: ", int(ans))
# 18700 too low
# this  answer is getting too complicated, lets try again


