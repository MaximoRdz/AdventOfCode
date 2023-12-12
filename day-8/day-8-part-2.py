import math

from itertools import cycle
from functools import reduce


with open("day-8/input.txt", "r") as file:
    guide, nodes = file.read().split("\n\n")

node_keys = [node.split(" = ")[0] for node in nodes.split("\n")]
node_values = []
for node in nodes.split("\n"):
    node = node.split(" = ")[1].replace(",", "").replace("(", "").replace(")", "")
    node_values.append(tuple(node.split()))

nodes = dict(zip(node_keys, node_values))


def check_end(current_points):
    # return boolean list same len
    return list(map(lambda s: s[-1] == "Z", current_points))

def next_points(current_points, s):
    next_nodes = []
    for current_node in current_points:
        next_nodes.append(nodes[current_node][s])
    return next_nodes


# find starting points
start_points = [p for p in node_keys if p[-1]=="A"]    # 6 starting points to keep track
start_points_period = dict().fromkeys(start_points)

current_points = start_points
reached = [False for _ in range(len(start_points))] # tracked the ones that finish
steps = 0
for s in cycle(guide):     
    if s == "L":
        next_nodes = next_points(current_points, 0)
    else:
        next_nodes = next_points(current_points, 1)

    steps += 1
    if any(check_end(next_nodes)): 
        # check which one reach the end, take its period 
        # assuming they are close loops from z to a and not to anywhere else
        for i, value in enumerate(check_end(next_nodes)):
            if value and not reached[i]:
                start_points_period[start_points[i]] = steps
                reached[i] = True
    elif all(check_end(next_nodes)):
        print("all done: ", steps)
        break
    
    if all(reached):
        print("all periods found")
        break


    if steps > 1e5:
        print("------ maximum steps reached")
        break

    current_points = next_nodes


def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)


print("solution part 2: ", reduce(lcm, start_points_period.values()))

