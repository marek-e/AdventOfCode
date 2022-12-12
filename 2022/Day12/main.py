#!/usr/bin/env python3

import numpy as np
import networkx as nx
import string

f = open('input.txt', 'r')


H = np.array([[*x.strip()] for x in f])

S = tuple(*np.argwhere(H == 'S'))
H[S] = 'a'
E = tuple(*np.argwhere(H == 'E'))
H[E] = 'z'

N = nx.grid_2d_graph(*H.shape).to_directed()

G = nx.DiGraph([(a, b) for a, b in N.edges()
                if ord(H[b]) <= ord(H[a])+1])

p = nx.shortest_path_length(G, target=E)
print('Part1 :', p[S])
print('Part2 :', min(p[a] for a in p if H[a] == 'a'))
