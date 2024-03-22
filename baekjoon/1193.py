import math

def nth_row_max_idx(n):
    return n * (n+1) // 2

def find_pos(X):
    row, col = 0, 0
    candidate = math.floor(math.sqrt(X * 2))
    candidate_max_idx = nth_row_max_idx(candidate)

    if candidate_max_idx < X:
        row = candidate + 1
        col = X - candidate_max_idx
    else:
        row = candidate
        col = candidate - (candidate_max_idx - X)

    return (row, col)

def find_expression(pos):
    numerator, denominator = 0, 0
    row, col = pos

    if row % 2 == 0:
        numerator = col
    else:
        numerator = row - (col - 1)
    denominator = row + 1 - numerator

    return str(numerator) + '/' + str(denominator)

X = int(input())
print( find_expression(find_pos(X)) )