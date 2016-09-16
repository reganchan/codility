# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    R = [ 0 ] * N
    for i in range( N ):
        prev = max( R[ max(0, i-6) : i ] ) if i > 0 else 0
        R[i] = prev + A[i]
    return R[-1]

