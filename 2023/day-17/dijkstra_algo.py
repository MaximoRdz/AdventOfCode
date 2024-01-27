from collections import deque
from heapq import heappop, heappush

""" SIMPLE WORKING EXAMPLE OF DIJKSTRA ALGORTIHM, SOME MODIFICATIONS MUST BE 
    MADE TO SOLVE TODAY'S PUZZLE. """


with open("day-17/example.txt", "r") as file:
    data = file.read().split("\n")

grid = [[int(s) for s in row] for row in data]
    
NROWS = len(grid)
NCOLS = len(grid[0])

def node_neighbors(i, j):
    # generate neighbors iterable
    connections = ((0, -1), (-1, 0), (0, 1), (1, 0))
    for ci, cj in connections:
        if 0<=i+ci<NROWS and 0<=j+cj<NCOLS:
            yield i+ci, j+cj

# nodes | dist | prev
# A     |   0  |  - 
# B     |  inf |  - 
# C     |  inf |  - 

# state = (distance, ic, jc, ip, jp)
priority_queue = [(0, 0, 0, 0, 0)]
visited = set()

while priority_queue:
    (d, i, j, ip, jp) = heappop(priority_queue)

    if (i, j) == (NROWS-1, NCOLS-1):
        print("Solution Part 1: ", d)
        break

    if (d, i, j, ip, jp) in visited:
        continue

    visited.add((d, i, j, ip, jp))

    for ni, nj in node_neighbors(i, j):
        heappush(priority_queue, (
            d+grid[ni][nj], 
            ni, nj, 
            i, j
        )
        )



# nodes = [(i, j) for j in range(NCOLS) for i in range(NROWS)]
# nodes = tuple(nodes)

# distance = {key:  1<<60 for key in nodes}    # current distance from source to key
# distance[(0, 0)] = 0   # source distance to source

# previous = {key: 0 for key in nodes}    # current previous node of key

# unvisited = deque(nodes)

# while len(unvisited) != 0:
#     # not visited node with less distance to source
#     u = min(unvisited, key=lambda x: distance[x])
#     # This way of programming is not appropiate, we're using a queue data structure where
#     # it shouldn't be used since the properties we require are not those a queue provides, 
#     # a simple queue works using the FIFO first in first out principle but here we're imposing
#     # with element according to the minimum distance rule, so what we are looking for is a priority
#     # queue based on distance 
#     # 
#     # The HEAP is one maximally efficient implementation of an abstract data type called a priority
#     # queue, and in fact, priority queues are often referred to as "heaps", regardless of how they
#     # may be implemented. In a heap, the highest (or lowest) priority element is always stored at 
#     # the root. However, a heap is not a sorted structure; it can be regarded as being partially 
#     # ordered. A heap is a useful data structure when it is necessary to repeatedly remove the object
#     # with the highest (or lowest) priority, or when insertions need to be interspersed with 
#     # removals of the root node.
#     unvisited.remove(u)

#     for neighbor in node_neighbors(u):
#         if neighbor in unvisited:
#             current_distance = distance[u] + grid[neighbor[0]][neighbor[1]]
#             if current_distance < distance[neighbor]:
#                 distance[neighbor] = current_distance
#                 previous[neighbor] = u

# print(distance[NROWS-1, NCOLS-1])




