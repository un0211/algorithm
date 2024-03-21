import sys

class IntegerStack (object):
    def __init__(self):
        self.stack = []
    
    def push(self, X):
        self.stack.append(X)
    
    def pop(self):
        if len(self.stack):
            # 스택이 비어있지 않은 경우
            print(self.stack.pop())
        else:
            # 스택이 비어있는 경우
            print(-1)

    def size(self):
        print(len(self.stack))
    
    def empty(self):
        if len(self.stack):
            print(0)
        else:
            print(1)
    
    def top(self):
        if len(self.stack):
            print(self.stack[-1])
        else:
            print(-1)


int_stack = IntegerStack()
num_of_instructions = int(sys.stdin.readline())

for i in range(num_of_instructions):
    instruction = sys.stdin.readline().split()
    
    if instruction[0] == "push":
        int_stack.push(int(instruction[1]))
    elif instruction[0] == "pop":
        int_stack.pop()
    elif instruction[0] == "size":
        int_stack.size()
    elif instruction[0] == "empty":
        int_stack.empty()
    elif instruction[0] == "top":
        int_stack.top()
