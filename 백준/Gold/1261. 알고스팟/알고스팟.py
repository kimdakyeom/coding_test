import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and dist[nx][ny] == -1:
                if arr[nx][ny] == 0:
                    dist[nx][ny] = dist[x][y]
                    queue.appendleft((nx, ny))
                else:
                    dist[nx][ny] = dist[x][y] + 1
                    queue.append((nx, ny))
    return dist


n, m = map(int, input().split())
arr = []
dist = [[-1] * n for _ in range(m)]
dist[0][0] = 0
for i in range(m):
    arr.append(list(map(int, input().rstrip())))
bfs(0, 0)
print(dist[m-1][n-1])