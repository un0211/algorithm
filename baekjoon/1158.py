#  연결리스트

N, K = ( int(x) for x in input().split() )

remains = [ n for n in range(1, N+1) ]  # 아직 남아있는 사람들
josephus = []   # 제거된 사람들 제거되는 순서대로

idx = 0
while remains:
    idx = (idx + K - 1) % len(remains)
    josephus.append(str(remains.pop(idx)))

print("<" + ', '.join(josephus) + ">")