#  연결리스트

import sys

for _ in range(int(sys.stdin.readline())):
    forward = []
    backward = []

    for c in sys.stdin.readline().strip():
        if c == '<':
            if forward:
                backward.append(forward.pop())
        elif c == ">":
            if backward:
                forward.append(backward.pop())
        elif c == "-":
            if forward:
                forward.pop()
        else:
            forward.append(c)
    
    backward.reverse()
    print(''.join(forward + backward))
