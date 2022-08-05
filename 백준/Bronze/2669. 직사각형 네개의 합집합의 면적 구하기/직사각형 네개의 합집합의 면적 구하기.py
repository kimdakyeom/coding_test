matrix = [[0] * 100 for _ in range(100)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    cnt = 0

    for i in range(x1, x2):
        for j in range(y1, y2):
            if matrix[i][j] == 0:
                matrix[i][j] = 1

    cnt = 0

    for i in range(100):
        for j in range(100):
            if matrix[i][j] == 1:
                cnt += 1
print(cnt)