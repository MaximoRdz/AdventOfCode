from itertools import combinations


with open("day-25/input.txt", "r") as file:
    data = file.read().splitlines()


connections = set()
vertices = set()
for line in data:
    key, *entries = line.replace(":", "").split()
    connections.update((key, elem) for elem in entries)
    vertices.add(key)
    vertices.update(entries)

# vertices = list(vertices)
N = len(vertices)


def connects_to(vertex, connections=connections):
    conns = filter(lambda conn: conn[0]==vertex or conn[1]==vertex, connections)
    for k, v in conns:
        if k==vertex:
            yield v
        if v==vertex:
            yield k


# def dfs(vertex, seen, connections):
#     seen.add(vertex)
#     for nvx in connects_to(vertex, connections):
#         if nvx not in seen:
#             dfs(nvx, seen, connections)
def dfs(vertex, seen, connections):
    stack = []
    stack.append(vertex)
    while stack:
        vx = stack.pop()
        if vx not in seen:
            seen.add(vx)
            for nvx in connects_to(vx, connections):
                stack.append(nvx)


for c1, c2, c3 in combinations(list(connections), 3):
    connections_copy = connections - set([c1, c2, c3])
    start_vx = list(vertices)[0]
    component_one = set()
    dfs(start_vx, component_one, connections_copy)
    if len(component_one) == N:
        continue
    component_two = set()
    start_vx = list(vertices-component_one)[0]
    dfs(start_vx, component_two, connections_copy)
    if len(component_two)+len(component_one)==N:
        print("Solution Part 1: ", len(component_two)*len(component_one))
        print("By disconecting: ", [c1, c2, c3])
        break

        
    

