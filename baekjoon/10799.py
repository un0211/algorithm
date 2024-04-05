num_sticks = 0    # 레이저 입장 아래에 쌓은 막대 수
total_sticks = 0  # 잘린 막대 전체 수
is_lazer = False

for c in input():
  if c == '(':
    num_sticks += 1  # 막대 시작
    is_lazer = True  # 레이저일 가능성 있음
    continue

  num_sticks -= 1  # 막대 끝 or 막대 아니라 레이저

  if is_lazer:
    total_sticks += num_sticks  # 내 아래 막대 다 자른다
  else:
    total_sticks += 1  # 막대 끝

  is_lazer = False

print(total_sticks)
