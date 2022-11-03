import networkx as nx
from kruskal import *
from time import time
import random


def test_kruskal(n):
    start = time()

    # Create graph for Kruskal's algorithm
    my_graph = Graph(n)
    vertices = {}

    # Create Networkx graph
    G = nx.Graph()

    # Create vertices
    for i in range(n):
        G.add_node(i)
        vertices[i] = Vertex1D(i)

    # Create edges
    for i in range(n-1):
        for j in range(i+1, n):
            w = random.uniform(0, 1)
            G.add_edge(i, j, weight=w)
            my_graph.edges.append((vertices[i], vertices[j], w))

    print(f'Graph building runtime: {time() - start} \n')

    # Run MST using Networkx
    start = time()
    mst = nx.algorithms.minimum_spanning_edges(G, algorithm="kruskal", data=True)
    sum = 0
    for edge in mst:
        sum += edge[2]['weight']
    print(f'Networknx MST Weight: {sum}')
    print(f'Networknx Runtime: {time() - start} \n')

    # Run MST using Kruskal's algorithm
    start = time()
    kruskal_mst, max_edge_cost = kruskal(my_graph)
    print(f'My MST Weight: {kruskal_mst.get_sum_weight()}')
    print(f'My MST Runtime: {time() - start}')


def test_kruskal_4d(n):
    start = time()

    # Create graph for Kruskal's algorithm
    my_graph = Graph(n)
    vertices = {}

    # Create Networkx graph
    G = nx.Graph()

    # Create vertices
    for i in range(n):
        G.add_node(i)
        vertices[i] = Vertex4D(i, random.uniform(0, 1),
                               random.uniform(0, 1),
                               random.uniform(0, 1),
                               random.uniform(0, 1))

    # Number of edges
    m = 0

    threshold = 2 / (n ** 0.25)

    # Create edges
    for p in range(n - 1):
        for q in range(p + 1, n):
            w = vertices[p].get_distance(vertices[q])
            G.add_edge(p, q, weight=w)
            if w < threshold:

                my_graph.edges.append((vertices[p], vertices[q], w))
                m += 1

    print(f'Graph building runtime: {time() - start} \n')

    # Run MST using Networkx
    start = time()
    mst = nx.algorithms.minimum_spanning_edges(G, algorithm="kruskal", data=True)
    sum = 0
    for edge in mst:
        sum += edge[2]['weight']
    print(f'Networknx MST Weight: {sum}')
    print(f'Networknx Runtime: {time() - start} \n')

    # Run MST using Kruskal's algorithm
    start = time()
    kruskal_mst, max_edge_cost = kruskal(my_graph)
    print(f'My MST Weight: {kruskal_mst.get_sum_weight()}')
    print(f'My MST Runtime: {time() - start}')

if __name__ == '__main__':
    test_kruskal_4d(n=2000)
