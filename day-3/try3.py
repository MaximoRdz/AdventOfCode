
with open("day-3/input.txt", "r") as file:
    lines = file.read().splitlines()

NROWS = len(lines)
NCOLS = len(lines[0])

def is_symbol(i, j):
    if not (0 <= i < NROWS and 0 <= j < NCOLS):
        return False
    else: 
        return not (lines[i][j] == "." or lines[i][j].isdigit())
        

ans = []

for i, line in enumerate(lines):
    start = 0  # number start
    j = 0 # line start

    while j < NCOLS:
        start = j
        number = ""
        while j < NCOLS and line[j].isdigit():
            number += line[j]
            j += 1
        
        if number == "":
            # ensure we complete the row even if we dont hit a number
            j += 1
            continue
        number = int(number)

        # number ended, look for adjacent
        # left and rigth to the number
        if is_symbol(i, start-1) or is_symbol(i, j):
            ans.append(number)
            continue
        # upper and lower sides of the number
        for k in range(start-1, j+1):
            if is_symbol(i-1, k) or is_symbol(i+1, k):
                ans.append(number)
                break


print(sum(ans))
