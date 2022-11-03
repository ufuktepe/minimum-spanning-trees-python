import math
import sys


class Vertex1D:
    def __init__(self, v_id, adj_vertices=None):
        self.id = v_id
        self.key = sys.maxsize

        # Adjacent vertices dictionary that maps vertices to their edge lengths
        if adj_vertices is None:
            self.adj = {}
        else:
            self.adj = adj_vertices

    def __lt__(self, other):
        return self.key < other.key

    def __gt__(self, other):
        return self.key > other.key

    def add_adj_vertex(self, other, weight):
        self.adj[other] = weight
        other.adj[self] = weight


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


if __name__ == '__main__':
    pass

