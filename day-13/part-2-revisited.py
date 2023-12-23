
with open("day-13/input.txt", "r") as file:
    patterns = file.read().split("\n\n")

patterns = [pattern.split("\n") for pattern in patterns]


def invert_pattern(pattern):
    inversed = []
    for j in range(len(pattern[0])):
        inversed.append("".join([pattern[i][j] for i in range(len(pattern))]))
    return inversed


inversed_patterns = [invert_pattern(pattern) for pattern in patterns]


def count_errors(pattern, n, m):
    result = 0
    for a, b in zip(pattern[n], pattern[m]):
        result += a!=b
    return result


def check_symmetry(pattern, n, m):
    if n == 0:
        return count_errors(pattern, n, m)
    if m == len(pattern)-1:
        return count_errors(pattern, n, m)

    smudges = count_errors(pattern, n, m)
    if n > 0 and m < len(pattern)-1:
        smudges += check_symmetry(pattern, n-1, m+1)
    
    return smudges

def check_pattern(pattern):
    NROWS = len(pattern)

    for axis in range(1, NROWS):
        n, m = axis-1, axis
        if check_symmetry(pattern, n, m) == 1:
            return axis
    return None

result = 0
for i, pattern in enumerate(patterns):
    row_smudge = check_pattern(pattern)
    column_smudge = check_pattern(inversed_patterns[i])

    if row_smudge is not None:
        result += 100*row_smudge
    elif column_smudge is not None:
        result += column_smudge
    else:
        print("-- ", i) 
        print("fatal error")

print("Solution part 2: ", result)
        




            




