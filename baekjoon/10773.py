#  스택

from collections import deque

int_que = deque()
for _ in range(int(input())):
    new_int = int(input())
    if new_int:
        int_que.append(new_int)
    else:
        int_que.pop()

print(sum(int_que))