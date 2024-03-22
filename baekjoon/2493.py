#  스택, 바킹독 솔루션 참고

from collections import deque


input() # consume n
heights = [ int(x) for x in input().split() ]

receiver_idx = []
buildings = deque([(100000001, 0)])

for i, height in enumerate(heights):
    while buildings[-1][0] < height:    # 나보다 낮은건 이제 내가 받는다
        buildings.pop()

    receiver_idx.append(buildings[-1][1])   # 나보다 높은 가장 가까운 놈
    buildings.append((height, i+1))

for i in receiver_idx:
    print(i, sep=' ')


# timeout

# # get input
# last_idx = int(input()) - 1
# heights = [ int(x) for x in input().split() ]

# # basic setting
# receiver_idx = [0] * (last_idx + 1) # 답 (건물번호)
# no_receiver = deque()   # 아직 수신자가 없는 빌딩 목록 (인덱스)

# while last_idx >= 0:
#     for _ in range(len(no_receiver)):
#         no = no_receiver.popleft()  # 수신자 없는 빌딩 하나씩 검사
#         if heights[last_idx] >= heights[no]:    # 수신자 발견
#             receiver_idx[no] = last_idx + 1
#         else:   # 수신자 미발견 -> 다시 목록에 추가
#             no_receiver.append(no)

#     no_receiver.append(last_idx)
#     last_idx -= 1

# for i in receiver_idx:
#     print(i, sep=' ')
