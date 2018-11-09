from itertools import permutations
from math import factorial

class Graph(object):
    """
    A class for undirected graphs.
    """

    def __init__(self, dic = dict()):
        self.dic = dic

    def vertices(self):
        """Vertices of a graph"""
        return tuple(self.dic.keys())

    def neighbors(self, vertex):
        """Set of neighbors of a given vertex in a graph"""
        if vertex in self.dic:
            return set(self.dic[vertex])
        else:
            return set()

    def edges(self):
        """Set of edges of a graph"""
        edges = set()
        for v in self.dic:
            neighbors = self.neighbors(v)
            for n in neighbors:
                if n > v: # Avoids adding edges twice
                    edges = edges.union({(v, n)})

        return edges

    def add_edge(self, edge):
        v1, v2 = edge # Unpack edge
        vertices = self.vertices()
        if (v1 in vertices) & (v2 in vertices):
            self.dic[v1].add(v2)
            self.dic[v2].add(v1)

    def add_edges(self, edges):
        for e in edges:
            self.add_edge(e)

    def del_edge(self, edge):
        v1, v2 = edge # Unpack edge
        vertices = self.vertices()
        if (v1 in vertices) & (v2 in vertices):
            self.dic[v1].remove(v2)
            self.dic[v2].remove(v1)

    def del_edges(self, edges):
        for e in edges:
            self.del_edge(e)

    def degree(self, vertex):
        if vertex in self.dic:
            neighbors = self.neighbors(vertex)
            return len(neighbors)
        else:
            return None

    def all_spines(self):
        """
        A generator of all possible spines from a graph's vertices,
        up to reversals, which we can ignore by symmetry
        """
        vertices = self.vertices()

        iterator = permutations(vertices)
        half_permutations = factorial(len(vertices))/2
        count = 0
        for spine in iterator:
            if count < half_permutations:
                count += 1
                yield spine
