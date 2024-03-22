#  배열 사용

A, B, C = (int(input()) for i in range(3))
mul = A * B * C

num_cnt = [0] * 10
while mul > 0:
    num_cnt[mul % 10] += 1
    mul //= 10

for n in num_cnt:
    print(n)