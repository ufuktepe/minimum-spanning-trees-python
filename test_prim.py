import networkx as nx
from prim import *
from time import time


def test_prim(n):
    start = time()

    # Vertices for Prim's algorithm
    vertices = []

    # Create Networkx graph
    G = nx.Graph()

    # Create vertices
    for i in range(n):
        G.add_node(i)
        vertices.append(Vertex1D(i))

    # Create edges
    for i in range(n-1):
        for j in range(i+1, n):
            w = random.uniform(0, 1)
            G.add_edge(i, j, weight=w)
            vertices[i].add_adj_vertex(vertices[j], w)

    print(f'Graph building runtime: {time() - start} \n')

    # Run MST using Networkx
    start = time()
    mst = nx.algorithms.minimum_spanning_edges(G, algorithm="prim", data=True)
    sum = 0
    for edge in mst:
        sum += edge[2]['weight']
    print(f'Networknx total cost: {sum}')
    print(f'Networknx runtime: {time() - start}\n')

    # Run MST using Prim's algorithm
    start = time()
    total_cost, max_edge_cost = prim(vertices)
    print(f'My MST total cost: {total_cost}')
    print(f'My MST runtime: {time() - start}')


if __name__ == '__main__':
    test_prim(n=1000)

