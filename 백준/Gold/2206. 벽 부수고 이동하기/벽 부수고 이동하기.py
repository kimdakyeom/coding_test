import sys
from pprint import pprint
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

arr = []

for i in range(n):
    arr.append(list(map(int, input().rstrip())))
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x, z):
    queue = deque()
    queue.append((y, x, z))
    while queue:
        y, x, z = queue.popleft()
        if y == n - 1 and x == m - 1:
            return visited[y][x][z]
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if arr[ny][nx] == 1 and z == 0:
                    queue.append((ny, nx, 1))
                    visited[ny][nx][1] = visited[y][x][0] + 1
                if arr[ny][nx] == 0 and visited[ny][nx][z] == 0:
                    queue.append((ny, nx, z))
                    visited[ny][nx][z] = visited[y][x][z] + 1
    return -1
print(bfs(0, 0, 0))