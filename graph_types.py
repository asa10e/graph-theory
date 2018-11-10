from Graph import Graph

def circulant(n = 0, num_set = {}):

    G = Graph({i: set() for i in range(0,n)})

    for i in range(0,n):
        for e in num_set:
            G.add_edge((i, (i+e)%n))

    return G

def complete(n):

    G = Graph({i: set() for i in range(0,n)})

    for i in range(0,n):
        i_neighbors = {v for v in range(0,n) if v != i}
        i_list = [i]*(n-1)
        edges_to_add = set(zip(i_neighbors, i_list))
        G.add_edges(edges_to_add)

    return G

def complete_bipartite(n,k):

    G = Graph({i: set() for i in range(0,n+k)})

    for v1 in G.vertices()[0:n]:
        for v2 in G.vertices()[n:n+k]:
            G.add_edge((v1,v2))

    return G

def path(n):

    G = Graph({i: set() for i in range(0,n)})

    for i in range(0,n-1):
        G.add_edges({(i,i+1)})

    return G

def path_power(n, k):

    G = path(n)

    for i in G.vertices():
        if i+k < n:
            G.add_edge((i,i+k))

    return G

def cycle(n):

    G = path(n)
    G.add_edge((0,n))

    return G

def star(n):

    G = Graph({i: set() for i in range(0,n)})

    for i in range(1,n):
        G.add_edge((0,i))

    return G
