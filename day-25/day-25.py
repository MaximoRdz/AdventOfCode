import networkx as nx 


with open("day-25/input.txt", "r") as file:
    data = file.read().splitlines()

graph = nx.Graph()

for line in data:
    key, *entries = line.replace(":", "").split()
    graph.add_edges_from((key, ent) for ent in entries)

graph.remove_edges_from(nx.minimum_edge_cut(graph))

G1, G2 = nx.connected_components(graph)

print("Solution Part 1: ", len(G1)*len(G2))