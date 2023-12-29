from collections import deque, defaultdict

with open("day-17/example.txt", "r") as file:
    data = file.read().split("\n")

grid = [[int(s) for s in row] for row in data]
NROWS = len(grid)
NCOLS = len(grid[0])

# nodes | dist | prev
# A     |   0  |  - 
# B     |  inf |  - 
# C     |  inf |  - 

nodes = [(i, j) for j in range(NCOLS) for i in range(NROWS)]
nodes = tuple(nodes)

distance = {key:  1<<60 for key in nodes}    # current distance from source to key
distance[(0, 0)] = 0   # source distance to source

previous = {key: 0 for key in nodes}    # current previous node of key

unvisited = deque(nodes)
visited = set()


while len(unvisited) != 0:
    # not visited node with less distance to source
    u = min(unvisited, key=lambda x: distance[x])
    unvisited.remove(u)
    visited.add(u)

    break

def dijkstra(weights, source, target):
    pass
    



