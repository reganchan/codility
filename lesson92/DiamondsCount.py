# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
from collections import defaultdict
from itertools import combinations

def solution(X, Y):
    # write your code in Python 2.7
    xs  = defaultdict( set )
    ys  = defaultdict( set )
    for x,y in zip( X, Y ):
        ys[ x ].add( y )
        xs[ y ].add( x )
    
    count = 0
    for x in ys.keys():
        for y1, y2 in combinations( ys[x], 2 ):
            if ( y1 + y2 ) % 2 == 1:
                continue
            ym = (y1+y2)/2
            
            for x1 in xs[ ym ]:
                if x1 == x:
                    continue
                x2 = 2*x-x1
                if x2 in xs[ ym ]:
                    count += 1
    
    return count / 2
        