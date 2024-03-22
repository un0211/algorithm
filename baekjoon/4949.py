import sys


def check_balance(s):
    parenthesis = []

    for c in s:
        if c in ["(", "["]:
            parenthesis.append(c)
        elif c == ")":
            if (not parenthesis) or (parenthesis.pop() != "("):
                return "no"
        elif c == "]":
            if (not parenthesis) or (parenthesis.pop() != "["):
                return "no"

    if parenthesis:
        return "no"

    return "yes"


in_str = sys.stdin.readline().rstrip()

while in_str != ".":
    print(check_balance(in_str))
    in_str = sys.stdin.readline().rstrip()