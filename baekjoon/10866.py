#  덱
import sys
from collections import deque

int_deq = deque()
for _ in range(int(input())):
    instr = sys.stdin.readline().split()

    if instr[0] == "push_front":
        int_deq.appendleft(int(instr[1]))
    elif instr[0] == "push_back":
        int_deq.append(int(instr[1]))
    elif instr[0] == "size":
        print(len(int_deq))
    elif instr[0] == "empty":
        print(int(not int_deq))
    elif not int_deq:
        print(-1)
    elif instr[0] == "pop_front":
        print(int_deq.popleft())
    elif instr[0] == "pop_back":
        print(int_deq.pop())
    elif instr[0] == "front":
        print(int_deq[0])
    elif instr[0] == "back":
        print(int_deq[-1])
