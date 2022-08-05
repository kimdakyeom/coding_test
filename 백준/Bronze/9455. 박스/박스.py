t = int(input())

for tc in range(t):

    m, n = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(m)]

    transposed_matrix = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            transposed_matrix[i][j] = matrix[j][i]

    cnt = 0

    for i in range(n):
        box_cnt = transposed_matrix[i].count(1)
        floor = m - 1

        for j in range(m-1, -1, -1):
            if transposed_matrix[i][j] == 1:
                cnt += floor - j
                floor -= 1

    print(cnt)