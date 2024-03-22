#  연결리스트

import sys


text_list = list(sys.stdin.readline().strip())
reversed_save = []

for _ in range(int(sys.stdin.readline())):
    inst = sys.stdin.readline().strip().split()
    
    if inst[0] == "L" and text_list:
        reversed_save.append(text_list.pop())
    elif inst[0] == "D" and reversed_save:
        text_list.append(reversed_save.pop())
    elif inst[0] == "B" and text_list:
        text_list.pop()
    elif inst[0] == "P":
        text_list.append(inst[1])

reversed_save.reverse()
print(''.join(text_list + reversed_save))


# timeout 코드

# text_list = list(sys.stdin.readline().strip())
# cursor = len(text_list)

# for _ in range(int(sys.stdin.readline())):
#     inst = sys.stdin.readline().strip().split()
    
#     if inst[0] == "L" and cursor > 0:
#         cursor -= 1
#     elif inst[0] == "D" and cursor < len(text_list):
#         cursor += 1
#     elif inst[0] == "B" and cursor > 0:
#         text_list.pop(cursor-1)
#         cursor -= 1
#     elif inst[0] == "P":
#         new_char = inst.split()[1]
#         text_list.insert(cursor, new_char)
#         cursor += 1

# print(''.join(text_list))