from collections import deque, defaultdict

""" SIMPLE WORKING EXAMPLE OF DIJKSTRA ALGORTIHM, SOME MODIFICATIONS MUST BE 
    MADE TO SOLVE TODAY'S PUZZLE. """


with open("day-17/example.txt", "r") as file:
    data = file.read().split("\n")

grid = [[int(s) for s in row] for row in data]
    
NROWS = len(grid)
NCOLS = len(grid[0])

def node_neighbors(coordinates):
    i, j = coordinates
    # generate neighbors iterable
    connections = ((0, -1), (-1, 0), (0, 1), (1, 0))
    for ci, cj in connections:
        if 0<=i+ci<NROWS and 0<=j+cj<NCOLS:
            yield i+ci, j+cj

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

    for neighbor in node_neighbors(u):
        if neighbor in unvisited:
            current_distance = distance[u] + grid[neighbor[0]][neighbor[1]]
            if current_distance < distance[neighbor]:
                distance[neighbor] = current_distance
                previous[neighbor] = u






