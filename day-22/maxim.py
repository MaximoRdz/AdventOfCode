

a, b = [1, 0, 1, 1, 2, 1], [0, 0, 2, 2, 0, 2]


c = min(a, b, key=lambda pos: pos[0])
print(c)