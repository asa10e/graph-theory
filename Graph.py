from itertools as it
import math
import numpy as np

class Graph(object):
    """
    A class for undirected graphs.
    Initialize with a dictionary of vertices as keys and lists of vertices as values.
    """
    def __init__(self, dic = dict()):
        self.dic = dic

    def vertices(self):
        """Vertices of a graph"""
        return tuple(self.dic.keys())

    def neighbors(self, vertex):
        """Set of neighbors of a given vertex"""
        if vertex in self.dic:
            return set(self.dic[vertex])
        else:
            return set()

    def edges(self):
        """Set of edges"""
        edges = set()
        for v in self.dic:
            neighbors = self.neighbors(v)
            for n in neighbors:
                if n > v: # Avoids adding edges twice
                    edges = edges.union({(v, n)})

        return edges

    def all_edges(self):
        """Set of edges of a graph, including reversals"""
        edges = set()
        for v in self.dic:
            neighbors = self.neighbors(v)
            for n in neighbors:
                edges = edges.union({(v, n)})

        return edges

    def add_edge(self, edge):
        """Adds an edge to the graph object"""
        v1, v2 = edge # Unpack edge
        vertices = self.vertices()
        if (v1 in vertices) & (v2 in vertices):
            self.dic[v1].add(v2)
            self.dic[v2].add(v1)

    def add_edges(self, edges):
        """Accepts a list of edges and calls add_edge on each one"""
        for e in edges:
            self.add_edge(e)

    def del_edge(self, edge):
        """Method to remove a given edge"""
        v1, v2 = edge # Unpack edge
        vertices = self.vertices()
        if (v1 in vertices) & (v2 in vertices):
            self.dic[v1].remove(v2)
            self.dic[v2].remove(v1)

    def del_edges(self, edges):
        """Accepts a list of edges and calls del_edge on each one"""
        for e in edges:
            self.del_edge(e)

    def degree(self, vertex):
        """Number of vertices distance 1 away from a given vertex"""
        if vertex in self.dic:
            neighbors = self.neighbors(vertex)
            return len(neighbors)
        else:
            return None

    def spines(self):
        """
        A generator of the possible spines from a graph's vertices
        up to reversals, which we can ignore by symmetry.
        """
        vertices = self.vertices()

        iterator = it.permutations(vertices)
        half_permutations = math.factorial(len(vertices))/2
        count = 0
        for spine in iterator:
            if count < half_permutations:
                count += 1
                yield spine

    def all_spines(self):
        """
        A generator of all  spines from a graph's vertices, including reversals
        """
        vertices = self.vertices()

        iterator = it.permutations(vertices)
        for spine in iterator:
            yield spine

    def matrix(self):
        """Graph's adjacency matrix"""
        dim = len(self.vertices())
        matrix = np.zeros((dim, dim), dtype=int)
        for e in self.all_edges():
            matrix[e[0], e[1]] = 1
        return matrix
    
