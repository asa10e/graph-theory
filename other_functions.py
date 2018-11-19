
def is_isomorphic(G, H):
    """
    Determines if two graphs are isomorphic.
    """
    if G.dic == H.dic:
        return True

    if len(G.vertices()) != len(H.vertices()):
        return False

    G_list = sorted([G.degree(i) for i in G.vertices()])
    H_list = sorted([H.degree(i) for i in H.vertices()])
    if G_list != H_list:
        return False

    P_G = Page(graph = G)
    for spine in G.all_spines():
        P_G.relabel(spine)
        if P_G.graph.dic == H.dic:
            return True

    return False
    
def matrix_to_dic(mat):

    l = len(mat)
    graph_dic = {i:set() for i in range(l)}

    for i in range(0, l):
        for j in range(0, l):
            if mat[i,j] == 1:
                graph_dic[i] = graph_dic[i].union({j})

    return graph_dic

def find_circulants(G):
    """
    Returns all distinct circulant graphs isomorphic to G.
    We can use this to create equivalance classes among circulants.
    """
    n = len(G.vertices())
    hit_list = []
    for i in range(1,n):
        num_sets = [set(e) for e in it.combinations(G.vertices(), i)]

        for j in num_sets:
            circ = circulant(n=n, num_set=j)
            if is_isomorphic(G, circ) == True:
                hit_list.append('circulant({0},{1})'.format(str(n), str(j)))

    return hit_list
