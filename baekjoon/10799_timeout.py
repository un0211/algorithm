sticks = []
lazers = []
stick_start = []
position = 0
num_sticks = 0

for c in input():
  if c == '(':
    stick_start.append(position)
    position += 1
    continue

  start = stick_start.pop()
  if position == start + 1:
    # 레이저는 점으로 생각
    lazers.append(start)
  else:
    # 스틱은 시작과 끝이 있는 막대로 생각
    sticks.append((start, position))
    position += 1

for stick in sticks:
  start, end = stick
  # 막대는 원래 한 개였는데 lazer 만날때마다 토막나서 한 개씩 늘어난다
  num_sticks += (1 + len(list(filter(lambda lazer: start < lazer and lazer < end, lazers))))

print(num_sticks)
