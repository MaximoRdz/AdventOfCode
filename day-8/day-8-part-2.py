from itertools import cycle

with open("day-8/input.txt", "r") as file:
    guide, nodes = file.read().split("\n\n")

node_keys = [node.split(" = ")[0] for node in nodes.split("\n")]
node_values = []
for node in nodes.split("\n"):
    node = node.split(" = ")[1].replace(",", "").replace("(", "").replace(")", "")
    node_values.append(tuple(node.split()))

nodes = dict(zip(node_keys, node_values))


def check_end(current_points):
    return all(map(lambda s: s[-1] == "Z", current_points))

def next_points(current_points, s):
    next_nodes = []
    for current_node in current_points:
        next_nodes.append(nodes[current_node][s])
    return next_nodes

steps = 0
# find starting points
start_points = [p for p in node_keys if p[-1]=="A"]
current_points = start_points
for s in cycle(guide):
    if s == "L":
        next_nodes = next_points(current_points, 0)
    else:
        next_nodes = next_points(current_points, 1)

    steps += 1
    if check_end(next_nodes):
        break
    
    if steps > 1e3:
        print("------ maximum steps reached")
        break

    current_points= next_nodes

print("solution part 2: ", steps)


# 1000001 is too low
