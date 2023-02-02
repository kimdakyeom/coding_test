import sys
from collections import deque
input = sys.stdin.readline

dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [0, -1, 1, -1, 1, -1, 0, 1]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    arr[y][x] = 0
    while queue:
        y, x = queue.popleft()
        for i in range(8):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and arr[ny][nx] == 1:
                queue.append((ny, nx))
                arr[ny][nx] = 0

m, n = map(int, input().split())
arr = []

for i in range(m):
    arr.append(list(map(int, input().split())))

cnt = 0
for i in range(m):
    for j in range(n):
        if arr[i][j] == 1:
            bfs(i, j)
            cnt += 1
print(cnt)