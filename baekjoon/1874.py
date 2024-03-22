#  스택

import sys
from collections import deque

que = deque()
max_n = 0
stack_instr = []
impossible = False

for _ in range(int(input())):
    top = int(sys.stdin.readline())

    if impossible:
        continue

    if top > max_n:
        for i in range(max_n+1, top):
            stack_instr.append('+')
            que.append(i)
        stack_instr.extend(['+', '-'])
        max_n = top
    else:
        if que and top == que.pop():
            stack_instr.append('-')
        else:
            impossible = True

if impossible:
    print('NO')
else:
    print('\n'.join(stack_instr))