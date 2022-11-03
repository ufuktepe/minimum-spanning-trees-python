from graph import *


def kruskal(graph):
    # Sort edges by edge length
    graph.edges.sort(key=lambda x: x[2])

    mst = Graph(graph.n)

    max_edge_cost = 0

    i, num_edges = 0, 0

    while num_edges < graph.n - 1:
        edge = graph.edges[i]

        vertex_1 = edge[0]
        vertex_2 = edge[1]

        if find_set(vertex_1) != find_set(vertex_2):
            union(vertex_1, vertex_2)
            mst.edges.append(edge)
            num_edges += 1

            # Update max edge cost
            if max_edge_cost < edge[2]:
                max_edge_cost = edge[2]

        i += 1

    return mst, max_edge_cost


def find_set(v):
    """
    Recursively finds the root of the tree containing vertex v.
    :param v: the given vertex
    :return: the root of the tree containing vertex v
    """
    if v.parent != v:
        v.parent = find_set(v.parent)
    return v.parent


def union(v1, v2):
    """
    Finds the roots of the sets containing vertices u and v and combines the two sets. The root with higher rank
    becomes the parent of the root with lower rank. If the two roots have equal rank, one of the roots is chosen
    arbitrarily as the parent and its rank is incremented.
    :param v1: first given vertex
    :param v2: second given vertex
    :return: None
    """
    root_v1 = find_set(v1)
    root_v2 = find_set(v2)

    if root_v1 == root_v2:
        return

    if root_v1.rank > root_v2.rank:
        root_v2.parent = root_v1
    else:
        root_v1.parent = root_v2
        if root_v1.rank == root_v2.rank:
            root_v1.rank += 1


def run(n_list, dim):

    output = []

    for n in n_list:

        # Build the graph
        if dim == 4:
            g, m = build_4d_graph(n)
        elif dim == 3:
            g, m = build_3d_graph(n)
        elif dim == 2:
            g, m = build_2d_graph(n)
        elif dim == 0:
            g, m = build_0d_graph(n)
        else:
            raise ValueError('Invalid dimension!')

        # Run MST using Kruskal's algorithm
        kruskal_mst, max_edge_cost = kruskal(g)

        output.append(kruskal_mst.get_sum_weight())

    return output


if __name__ == '__main__':
    pass
