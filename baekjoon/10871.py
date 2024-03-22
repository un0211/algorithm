N, X = ( int(x) for x in input().split() )
A = [ x for x in input().split() if int(x) < X ]

print(' '.join(A))