
with open("day-23/input.txt", "r") as file:
    data = file.read().splitlines()

# ##############
# ###S####   ###     
# ### #### #####     
# ###  i   ##### 
# ##### ######## 
# ##############
    
# Edge contraction: Since the map is mazze-like we can 
# contract the graph to take into account only point of 
# interest (i) (that is points with more than 2 neighbors)  
# and the distance between them
NROWS, NCOLS = len(data), len(data[0])
# Identify Cross Road points
start = 0, data[0].index(".")
end = NROWS-1, data[-1].index(".")

points = [start, end]
for i, line in enumerate(data):
    for j, ch in enumerate(line):
        if ch=="#":
            continue
        neighbors = 0
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if (0<=ni<NROWS and 0<=nj<NCOLS) and data[ni][nj]!="#":
                neighbors += 1 
        if neighbors >= 3:
            points.append((i, j))
    
# Reconstrut the grid with a graph containing only points
# points of interest
# Because there is only one possible straight path from 
# interest point to interest point we can construct this 
# graph by defining connections with length equivalent
# to the steps it take to go from A to B

# adjacent to list
graph = {pt: {} for pt in points}

for si, sj in points:
    stack = [(0, si, sj)]
    seen = {(si, sj)}

    while stack:
        n, i, j = stack.pop()

        if n!=0 and (i, j) in points:
            graph[(si, sj)][(i, j)] = n
            continue

        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = i+di, j+dj
            if (0<=ni<NROWS and 0<=nj<NCOLS) and (data[ni][nj]!="#") and ((ni, nj) not in seen):
                stack.append((n+1, ni, nj))
                seen.add((ni, nj))

visited = set()
def depth_first_search(vertex):

    if vertex == end:
        return 0
    
    max_steps = -float("inf")

    visited.add(vertex)
    for nv in graph[vertex]:
        if nv not in visited:
            max_steps = max(max_steps, depth_first_search(nv)+graph[vertex][nv])
    visited.remove(vertex)

    return max_steps

print("Solution Part 2: ", depth_first_search(start))






