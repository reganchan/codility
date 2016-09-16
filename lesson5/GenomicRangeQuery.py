from itertools import starmap

def solution(S, P, Q):
    # write your code in Python 2.7
    N = len( S )
    A, C, G, T = [ [0] * (N+1) for i in range(4) ]
    
    for i, s in enumerate( S, start=1 ):
        v = 'ACGT'.index( s )+1
        for ACGT in A,C,G,T:
            ACGT[ i ] = ACGT[ i-1 ]
        ACGT = (A,C,G,T)[ v-1 ]
        ACGT[ i ] += v
    
    def M( p, q ):
        for v, ACGT in enumerate( (A, C, G, T), start=1 ):
            if 0 < ACGT[q+1] - ACGT[p]:
                return v
        
    output = list(starmap( M, zip( P, Q ) ))
    return output