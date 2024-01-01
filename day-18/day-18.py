from collections import defaultdict



with open("day-18/input.txt", "r") as file:
    data = file.read().splitlines()



directions = {"R": (0, 1), "L": (0, -1), "U": (-1, 0), "D": (1, 0)}

lagoon_edge = set()

start_point = (0, 0)
lagoon_edge.add(start_point)

pi, pj = start_point
for line in data:
    direction, units, color = line.split()

    units = int(units)
    di, dj = directions[direction]
    
    for _ in range(units):
        ni, nj = pi+di, pj+dj
        lagoon_edge.add((ni, nj))
        pi, pj = ni, nj


MIN_X = min(lagoon_edge, key=lambda j: j[1])[1]
MAX_X = max(lagoon_edge, key=lambda j: j[1])[1]
MIN_Y = min(lagoon_edge, key=lambda i: i[0])[0]
MAX_Y = max(lagoon_edge, key=lambda i: i[0])[0]



result = 0
for i in range(MIN_Y, MAX_Y+1):
    for j in range(MIN_X, MAX_X+1):
        if (i, j) in lagoon_edge:
            continue
        crosses = 0
        for k in reversed(range(MIN_X, j+1)):
            if (i, k) in lagoon_edge and (i, k+1) not in lagoon_edge and (i, k-1) not in lagoon_edge:
                crosses += 1
            if (i, k) in lagoon_edge and (i, k+1) not in lagoon_edge and (i, k-1) in lagoon_edge:
                crosses += 1
        result += crosses % 2
    

            
result += len(lagoon_edge)
print("Solution Part 1: ", result)


