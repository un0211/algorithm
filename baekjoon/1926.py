paper = []
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
n = 0
max_area = 0

row, col = [int(x) for x in input().split()]

for _ in range(row):
    paper.append([int(x) for x in input().split()])

for x in range(row):
    for y in range(col):
        if paper[x][y] == 0:
            continue

        piece = [(x, y)]
        paper[x][y] = 0
        n += 1
        area = 0

        while piece:
            cx, cy = piece.pop()
            area += 1

            for i in range(4):
                nx = cx + dx[i]
                ny = cy + dy[i]

                if nx < 0 or ny < 0 or nx >= row or ny >= col:
                    continue
                if paper[nx][ny] == 0:
                    continue

                piece.append((nx, ny))
                paper[nx][ny] = 0

        max_area = max(max_area, area)

print(n)
print(max_area)