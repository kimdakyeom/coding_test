import sys
sys.setrecursionlimit(100000)

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]
        if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0:
            cnt += 1
            dfs(nx, ny)

m, n, k = map(int, input().split())
visited = [[0] * n for _ in range(m)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for t in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            visited[i][j] = 1

area = 0
cnt = 1
answer = []

for i in range(m):
    for j in range(n):
        if visited[i][j] == 0:
            area += 1
            dfs(i, j)
            answer.append(cnt)
            cnt = 1

answer.sort()
print(area)
print(*answer, end=' ')