num_good_words = 0

for _ in range(int(input())):
  word = input()
  stack = []

  for c in word:
    if stack and stack[-1] == c:
      stack.pop()
      continue

    stack.append(c)
  
  if not stack:
    num_good_words += 1

print(num_good_words)
