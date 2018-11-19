from Graph import Graph
class Page(object):
    """
    A Page is a Graph fixed along a spine (a permutation of the Graph's vertices)
    """
    def __init__(self, spine = None, graph = None):

        if graph == None:
            graph = Graph({s:set() for s in spine})

        if spine == None:
            spine = graph.vertices()

        self.spine = spine
        self.graph = graph

    def relabel(self, new_spine = None):

        if new_spine == None:
            new_spine = tuple(sorted([i for i in self.spine]))

        assert sorted(new_spine) == sorted(self.spine), "new_spine must be a permutation of the page's spine"

        # Permutation takes current spine to new_spine
        permutation = dict(zip(self.spine, new_spine))
        #permutation = {s:self.spine.index(s) for s in new_spine}
        perm_dic = {permutation[i]:set([permutation[n] for n in self.graph.neighbors(i)]) for i in self.spine}

        self.spine = new_spine
        self.graph = Graph(perm_dic)

    # def standardize(self):
    #     """
    #     Relabels the page such that the spine is in a (0,1,2,...) order,
    #     and adjusts its edges accordingly
    #     """
    #     permutation = {s:self.spine.index(s) for s in self.spine}
    #     # idx_to_s = {idx:s for s, idx in permutation.items()} # to reverse later if desired
    #     perm_dic = {permutation[i]:[permutation[n] for n in self.graph.neighbors(i)] for i in self.spine}
    #     #mapped_dic = Graph(perm_dic)
    #
    #     self.spine = sorted(self.spine)
    #     self.graph = Graph(perm_dic)

    def has_intersections(self):
        """
        True if the page's edges cross at least once
        False otherwise
        """
        # TODO we could use .relabel() here instead
        permutation = {s:self.spine.index(s) for s in self.spine}
        idx_to_s = {idx:s for s, idx in permutation.items()} # to reverse later if desired
        perm_dic = {permutation[i]:[permutation[n] for n in self.graph.neighbors(i)] for i in self.spine}
        perm_graph = Graph(perm_dic)

        for i in perm_graph.vertices():

            j_keys = tuple([k for k in perm_graph.neighbors(i) if k>i])
            for j in j_keys:
                '''
                There is a crossing if:
                i has a neighbor n above j and either:
                    j has a neighbor below i
                    or
                    j has a neighbor above n
                '''
                # TODO change to min max thing
                for i_n in perm_graph.neighbors(i):
                    if i_n > j:
                        for j_n in perm_graph.neighbors(j):
                            if (j_n < i) | (j_n > i_n):
                                # print('{0}: {1}-{2} X {3}-{4}'.format(self.spine, idx_to_s[i], idx_to_s[i_n], idx_to_s[j], idx_to_s[j_n]))
                                return True
        return False
