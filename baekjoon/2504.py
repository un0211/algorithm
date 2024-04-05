def get_result():
  stack = []        # 여는 괄호 수집
  add_list = [[]]   # 단계별 완성된 수 모음

  start = ['(', '[']
  end = [')', ']']
  value = [2, 3]

  multiply = False

  for c in input():
    if c == '(' or c == '[':
      stack.append(c)
      add_list.append([]) # 새 단계 시작
      multiply = False
      continue

    if not stack:
      return 0

    idx = end.index(c)
    if stack.pop() != start[idx]:
      return 0
    
    partial_result = sum(add_list.pop())  # 이번 단계 끝

    if multiply:
      partial_result *= value[idx]
    else:
      partial_result += value[idx]
      multiply = True

    add_list[-1].append(partial_result)  # 이전 단계에 반영

  if stack:
    return 0
    
  return sum(add_list[-1])

print(get_result())
