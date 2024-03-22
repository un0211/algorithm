#  큐
import sys
from collections import deque

int_que = deque()

for _ in range(int(input())):
    instr = sys.stdin.readline().split()

    if instr[0] == "push":
        int_que.append(int(instr[1]))
    elif instr[0] == "size":
        print(len(int_que))
    elif instr[0] == "empty":
        print(int(not int_que))
    elif not int_que:
        print(-1)
    elif instr[0] == "pop":
        print(int_que.popleft())
    elif instr[0] == "front":
        print(int_que[0])
    elif instr[0] == "back":
        print(int_que[-1])
