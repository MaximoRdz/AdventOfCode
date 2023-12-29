from collections import deque

"""
CONSTRAINS: 
1) 
Because it is difficult to keep the top-heavy crucible 
going in a straight line for very long, it can move at 
most three blocks in a single direction before it must 
turn 90 degrees left or right.
2)
The crucible also can't reverse direction; after 
entering each city block

Dijkstra algorithm already meets (2) by default
"""

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

# dijkstra algorithm
# nodes | dist | prev
# A     |   0  |  - 
# B     |  inf |  - 
# C     |  inf |  - 

nodes = [(i, j) for j in range(NCOLS) for i in range(NROWS)]
nodes = tuple(nodes)

distance = {key:  1<<60 for key in nodes}    # current distance from source to key
distance[(0, 0)] = 0   # source distance to source

previous = {key: (0, 0) for key in nodes}    # current previous node of key


def is_allowed(neighbor, u):
    count_i = 0
    count_j = 0
    n = 0
    p = u
    while n<4:
        count_i += p[0]==neighbor[0]
        count_j += p[1]==neighbor[1]
        if p == (0, 0):
            break
        neighbor = p
        p = previous[neighbor]
        n += 1
    if count_i>3 or count_j>3:
        return False
    else:
        return True


unvisited = deque(nodes)
visited = set()

while len(unvisited) != 0:
    # not visited node with less distance to source
    u = min(unvisited, key=lambda x: distance[x])
    unvisited.remove(u)
    visited.add(u)

    if u == (NROWS-1, NCOLS-1):
        print(distance[u])

    for neighbor in node_neighbors(u):
        if neighbor in unvisited and is_allowed(neighbor, u):
            current_distance = distance[u] + grid[neighbor[0]][neighbor[1]]
            if (current_distance<distance[neighbor]):
                distance[neighbor] = current_distance
                previous[neighbor] = u
    
    
"""
SOMEHOW I NEED TO INTRODUCE THE DIRECTION WE ARE MOVING IN THE STATE VARIABLES
"""


def plot_path():
    # blocks_map = [[str(grid[i][j]) for j in range(NCOLS)] for i in range(NROWS)]    
    blocks_map = [[" " for j in range(NCOLS)] for i in range(NROWS)]    

    blocks_map[NROWS-1][NCOLS-1] = "#"
    blocks_map[0][0] = "#"

    p = previous[(NROWS-1, NCOLS-1)]
    while p != (0, 0):
        blocks_map[p[0]][p[1]] = "#"
        p = previous[p]
    print(*blocks_map, sep="\n")


print("Solution part 1: ", distance[(NROWS-1, NCOLS-1)])
plot_path()







