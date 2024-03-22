# 배열만 써서 풀어보자.

in_str = input()
num_chars = [0] * 26

for c in in_str:
    num_chars[ord(c) - 97] += 1  # ord('a') == 97

for n in num_chars:
    print(n, end=' ')