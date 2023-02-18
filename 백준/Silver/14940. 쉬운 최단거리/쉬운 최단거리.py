import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

n, m = map(int, input().split())
visited = [[-1] * m for _ in range(n)]
arr = []
cnt = 0

for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if arr[i][j] == 2:
            bfs(i, j)
        elif arr[i][j] == 0:
            visited[i][j] = 0

for i in range(n):
    print(*visited[i])