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
DOWNHILL2DIR = {v: k for k, v in DIR2DOWNHILL.items()}

SLOPES = set("<>v^")
# state: 
# neg_steps, i, j, last_uphill
# neg_steps: pop smallest then we negate steps to ensure
#            largest path possible
# last_uphill: "<" if the last hill was up
initial_state = 0, st[0], st[1], ""
q = [initial_state]
visited = set()
while q:
    neg_steps, i, j, last_slope = heappop(q)
    
    if (i, j) == nd:
        print("Solution Part 1: ", -neg_steps)
        
    if (i, j) in visited:
        continue

    visited.add((i, j))
    
    if last_slope:
        di, dj = DOWNHILL2DIR[last_slope]
        ni, nj = i+di, j+dj
        if not (0<=ni<NROWS and 0<=nj<NOCLS) or route_map[ni][nj] == "#":
            continue
        new_slope = ""
        if route_map[ni][nj] in SLOPES:
            new_slope = route_map[ni][nj]
        heappush(q, (neg_steps-1, ni, nj, new_slope))
        continue


    for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        ni = i + di
        nj = j + dj

        if not (0<=ni<NROWS and 0<=nj<NOCLS) or route_map[ni][nj] == "#":
            continue

        if route_map[ni][nj] in SLOPES:
            new_slope = route_map[ni][nj]
            heappush(q, (neg_steps-1, ni, nj, new_slope))

            # uphill = DIR2UPHILL[(di, dj)]
            # downhill = SLOPES-set(uphill) # what is not uphill
            # if not last_slope and route_map[ni][nj] == uphill: 
            #     heappush(q, (neg_steps-1, ni, nj, 1))
            # if not last_slope and route_map[ni][nj] != uphill: 
            #     heappush(q, (neg_steps-1, ni, nj, 0))
            # if last_slope and route_map[ni][nj] not in downhill:
            #     continue
            # if last_slope and route_map[ni][nj] in downhill:
            #     heappush(q, (neg_steps-1, ni, nj, 0))
        else:
            heappush(q, (neg_steps-1, ni, nj, last_slope))





        