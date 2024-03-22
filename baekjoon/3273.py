# 배열 사용

n_pair = 0
check_appeared = [0] * 1000001

# get input
n = int(input())
int_arr = [ int(x) for x in input().split() ]
x = int(input())

for i in int_arr:
    if x-i <= 1000000 and check_appeared[x-i]:
        n_pair += 1
        # no duplication -> no need to check
    else:
        check_appeared[i] = 1

print(n_pair)