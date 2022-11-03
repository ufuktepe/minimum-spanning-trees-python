import math
import random


class Graph:
    def __init__(self, num_vertices):
        self.n = num_vertices
        self.edges = []  # Each edge is a tuple of (vertex1, vertex2, length)

    def get_sum_weight(self):
        sum = 0
        for edge in self.edges:
            sum += edge[2]
        return sum


class Vertex1D:
    def __init__(self, v_id):
        self.id = v_id
        self.parent = self
        self.rank = 0


class Vertex2D(Vertex1D):
    def __init__(self, v_id, x, y):
        super(Vertex2D, self).__init__(v_id)
        self.x = x
        self.y = y

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Vertex3D(Vertex2D):
    def __init__(self, v_id, x, y, z):
        super(Vertex3D, self).__init__(v_id, x, y)
        self.z = z

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)


class Vertex4D(Vertex3D):
    def __init__(self, v_id, x, y, z, t):
        super(Vertex4D, self).__init__(v_id, x, y, z)
        self.t = t

    def get_distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2 + (self.t - other.t)**2)


def build_4d_graph(n):
    # Create graph
    g = Graph(n)

    # Dictionary to access vertices
    vertices = {}

    threshold = 2 / (n**0.25)

    # Create the vertices
    for j in range(n):
        vertices[j] = Vertex4D(j, random.uniform(0, 1),
                               random.uniform(0, 1),
                               random.uniform(0, 1),
                               random.uniform(0, 1))

    return create_edges(g, n, vertices, threshold)


def build_3d_graph(n):
    # Create graph
    g = Graph(n)

    # Dictionary to access vertices
    vertices = {}

    threshold = 1.8 / (n ** 0.3)

    # Create the vertices
    for j in range(n):
        vertices[j] = Vertex3D(j, random.uniform(0, 1),
                               random.uniform(0, 1),
                               random.uniform(0, 1))

    return create_edges(g, n, vertices, threshold)


def build_2d_graph(n):
    # Create graph
    g = Graph(n)

    # Dictionary to access vertices
    vertices = {}

    threshold = 1.5 / (n ** 0.4)

    # Create the vertices
    for j in range(n):
        vertices[j] = Vertex2D(j, random.uniform(0, 1),
                               random.uniform(0, 1))

    return create_edges(g, n, vertices, threshold)


def build_0d_graph(n):
    # Create graph
    g = Graph(n)

    # Dictionary to access vertices
    vertices = {}

    threshold = 20 / n

    # Create the vertices
    for j in range(n):
        vertices[j] = Vertex1D(j)

    # Number of edges
    m = 0

    # Create edges
    for p in range(n - 1):
        for q in range(p + 1, n):
            w = random.uniform(0, 1)

            if w < threshold:
                g.edges.append((vertices[p], vertices[q], w))
                m += 1

    return g, m


def create_edges(g, n, vertices, threshold):
    # Number of edges
    m = 0

    # Create edges
    for p in range(n - 1):
        for q in range(p + 1, n):
            w = vertices[p].get_distance(vertices[q])

            if w < threshold:
                g.edges.append((vertices[p], vertices[q], w))
                m += 1

    return g, m


if __name__ == '__main__':
    pass

