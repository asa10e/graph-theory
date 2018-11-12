def page_split(page, edges):
    """
    page: A Page object
    edges: a set of tuples such as {(1,3), (5,9)}
    Outputs a tuple of two pages.
    The Graphs will have the same vertices, but the edges in edges are removed
    in one and added to the other.
    """
    page1 = deepcopy(page) # We don't want to change the underlying graph object
    page2 = Page(page1.spine)

    for edge in edges:
        v1 = edge[0]
        v2 = edge[1]

        # If v1-v2 is in page1
        if (v2 in page1.graph.neighbors(v1)) and (v1 in page1.graph.neighbors(v2)):

            # Remove edge from page1
            page1.graph.del_edge((v1,v2))

            # Add edge to page2
            page2.graph.add_edge((v1,v2))

    return (page1, page2)

def bt1(G):
    """
    Determines if a graph has book thickness 1
    """
    for spine in G.spines():
        P = Page(spine, G)
        if P.has_intersections() == False:
            print('A configuration of book thickness 1 is: {}'.format(spine))
            return True
    print('The graph has book thickness greater than 1')
    return False

def bt2(G):
    """
    Determines if a graph has book thickness 2
    """
    for spine in G.spines():
        P = Page(spine, G)

        iterables = (it.combinations(G.edges(), i) for i in range(1, len(G.edges())))
        for combos in iterables:
            for combo in combos:
                p1, p2 = page_split(P, list(combo))
                B = Book({p1,p2})
                if B.is_nice_embedding() == True:
                    print('Nice book embedding found!')
                    return B
    print('Graph does not have book thickness 2')
    return None
