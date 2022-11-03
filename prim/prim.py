from vertex import *
from min_heap import MinHeap
import random
from time import time


def prim(vertices):

    root = vertices[0]
    root.key = 0

    # Create a minimum priority queue, takes O(nlog(n)) time.
    min_pq = MinHeap(vertices)

    # Total cost of the MST
    cost = 0

    max_edge_cost = 0

    while min_pq.items:

        # Extract the minimum item, takes O(log(n)) time
        min_item = min_pq.extract_min()

        cost += min_item.key

        # Update max edge cost
        if max_edge_cost < min_item.key:
            max_edge_cost = min_item.key

        # iterate over the adjacent vertices
        for v, weight in min_item.adj.items():
            if v.id in min_pq.idx_dict and v.key > weight:
                v.key = weight

                # Find the index of v in the heap and decrease its key value, takes O(log(n)) time.
                v_idx = min_pq.idx_dict[v.id]
                min_pq.heap_decrease_key(v_idx, weight)

    return cost, max_edge_cost


def run(iter):
    print('Running Prim')

    n_list = [128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144]

    print('n,m,Graph creation runtime,MST Cost,Max Edge Cost,MST Runtime')

    for n in n_list:
        for i in range(iter):
            start = time()

            # Vertices for Prim's algorithm
            vertices = []

            # Create vertices
            for i in range(n):
                vertices.append(Vertex1D(i))

            threshold = 20 / n

            # Number of edges
            m = 0

            # Create edges
            for i in range(n - 1):
                for j in range(i + 1, n):
                    w = random.uniform(0, 1)
                    if w < threshold:
                        vertices[i].add_adj_vertex(vertices[j], w)
                        m += 1

            graph_creation_runtime = round(time() - start)

            # Run MST using Prim's algorithm
            start = time()
            total_cost, max_edge_cost = prim(vertices)
            mst_runtime = round(time() - start)
            print(f'{n},{m},{graph_creation_runtime},{total_cost},{max_edge_cost},{mst_runtime}')

    print('DONE!')


if __name__ == '__main__':
    pass



