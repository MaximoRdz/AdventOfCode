from itertools import cycle

with open("day-8/input.txt", "r") as file:
    guide, nodes = file.read().split("\n\n")

node_keys = [node.split(" = ")[0] for node in nodes.split("\n")]
node_values = []
for node in nodes.split("\n"):
    node = node.split(" = ")[1].replace(",", "").replace("(", "").replace(")", "")
    node_values.append(tuple(node.split()))

nodes = dict(zip(node_keys, node_values))



steps = 0
current_node = "AAA"
for s in cycle(guide):
    if s == "L":
        next_node = nodes[current_node][0]
    else:
        next_node = nodes[current_node][1]

    steps += 1
    if next_node == "ZZZ":
        break
    
    if steps > 1e6:
        print("maximum steps reached")
        break

    current_node = next_node

print("solution part 1: ", steps)