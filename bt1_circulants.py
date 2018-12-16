from graph_types import circulant
from book_thickness import bt1, bt2
import itertools as it

import io
import sys

def hide_prints(func):
    def wrapper(*args, **kwargs):
        sys.stdout = io.StringIO() # Hide away stdout
        out = func(*args, **kwargs) # Store the function to return
        sys.stdout = sys.__stdout__ # Bring stdout back
        return out
    return wrapper

@hide_prints
def make_circ_list(n, k):
    out_dic = dict()
    for i in range(k, n+1):
        for num_set in it.combinations(list(range(i)), k):
            G = circulant(i, num_set)
            if bt1(G) == True:
                out_dic[(n, num_set)] = 'bt1'
            # elif bt2(G) == True:
            #     out_dic[(n, num_set)] = 'bt2'
            else:
                out_dic[(n, num_set)] = 'Other'


    lis = sorted([x[1] for x in out_dic])
    return lis
