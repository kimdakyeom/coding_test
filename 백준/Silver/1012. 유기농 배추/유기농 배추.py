for t in range(int(input())):
    m, n, k = map(int, input().split())

    arr = [[0] * m for i in range(n)]
    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0

    def dfs(arr, i, j):
        stack = [[i, j]]
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while stack:
            a, b = stack.pop()
            arr[a][b] = 0
            for i in range(4):
                x = a + dx[i]
                y = b + dy[i]
                if 0 <= x < n and 0 <= y < m and arr[x][y] == 1:
                    arr[x][y] == 0
                    stack.append([x, y])

    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                cnt += 1
                dfs(arr, i, j)
    print(cnt)