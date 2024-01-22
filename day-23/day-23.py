from heapq import heappop, heappush


with open("day-23/example.txt", "r") as file:
    data = file.read().splitlines()

route_map = [[s for s in line] for line in data]

NROWS, NOCLS = len(route_map), len(route_map[0])

st = 0, data[0].find(".")
nd = NROWS-1, data[-1].find(".")

DIR2UPHILL = {
    (0, 1) : "<",
    (0, -1): ">",
    (1, 0): "^", 
    (-1, 0): "v"
}
DIR2DOWNHILL = {
    (0, 1) : ">",
    (0, -1): "<",
    (1, 0): "v", 
    (-1, 0): "^"
}
SLOPES = set("<>v^")
# state: 
# neg_steps, i, j, last_uphill
# neg_steps: pop smallest then we negate steps to ensure
# largest path possible
# last_uphill: 1 if the last hill was up
initial_state = 0, st[0], st[1], 0
q = [initial_state]
visited = set()
while q:
    neg_steps, i, j, last_hill = heappop(q)

    if (i, j) == nd:
        print("Solution Part 1: ", -neg_steps)
    
    if (i, j, last_hill) in visited:
        continue

    visited.add((i, j, last_hill))
    
    for di,dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni = i + di
        nj = j + dj

        if not (0<=ni<NROWS and 0<=nj<NOCLS) or route_map[ni][nj] == "#":
            continue

        if route_map[ni][nj] in SLOPES:
            uphill = DIR2UPHILL[(di, dj)]
            downhill = SLOPES-set(uphill) # what is not uphill


            if not last_hill and route_map[ni][nj] == uphill: 
                heappush(q, (neg_steps-1, ni, nj, 1))
                continue
            if not last_hill and route_map[ni][nj] != uphill: 
                heappush(q, (neg_steps-1, ni, nj, 0))
                continue
            if last_hill and route_map[ni][nj] not in downhill:
                continue
            if last_hill and route_map[ni][nj] in downhill:
                heappush(q, (neg_steps-1, ni, nj, 0))
                continue
        else:
            heappush(q, (neg_steps-1, ni, nj, last_hill))





        