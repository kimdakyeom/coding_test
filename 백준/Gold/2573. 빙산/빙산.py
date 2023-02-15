import sys
input = sys.stdin.readline
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    global cnt
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] != 0 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    queue.append((nx, ny))
                elif arr[nx][ny] == 0:
                    cnt[x][y] += 1
    return 1

n, m = map(int, input().split())
arr = []
flag = False
ans = 0

for i in range(n):
    arr.append(list(map(int, input().split())))

while True:
    visited = [[0] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]
    result = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and visited[i][j] == 0:
                result += bfs(i, j)
    for i in range(n):
        for j in range(m):
            arr[i][j] -= cnt[i][j]
            if arr[i][j] < 0:
                arr[i][j] = 0
    if result == 0:
        break
    if result >= 2:
        flag = True
        break
    ans += 1

if flag:
    print(ans)
else:
    print(0)