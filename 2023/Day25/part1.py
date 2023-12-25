import networkx as nx

f = open("input.txt", "r")

graph = nx.Graph(
    [
        (line.split(":")[0], x)
        for line in f.read().splitlines()
        for x in line.split(":")[1].strip().split(" ")
    ]
)
graph.remove_edges_from(nx.minimum_edge_cut(graph))
print(
    len(list(nx.connected_components(graph))[0])
    * len(list(nx.connected_components(graph))[1])
)
