N, M = [int(x) for x in input().split()]
positions = [int(x) for x in input().split()]
offsets = [0] * M

pointer = 1
num_ops = 0

for i in range(M):
    position = positions[i] + offsets[i]

    for j in range(i+1, M):
        if positions[j] + offsets[j] > position:
            offsets[j] -= 1

    if pointer == position:
        N -= 1
        continue

    left_ops = (position - pointer) % N
    if left_ops > N / 2:
        num_ops += (N - left_ops)
    else:
        num_ops += left_ops

    pointer = position
    N -= 1

print(num_ops)