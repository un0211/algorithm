#  배열 사용
import math


cnt_ns = [0] * 10
room_n = int(input())

while room_n > 0:
    cnt_ns[room_n % 10] += 1
    room_n //= 10

cnt_ns[6] = math.ceil((cnt_ns[6] + cnt_ns[9]) / 2)
cnt_ns.pop()
print(max(cnt_ns))