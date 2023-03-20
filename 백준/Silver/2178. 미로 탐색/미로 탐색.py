import sys
input = sys.stdin.readline
from collections import deque
from pprint import pprint

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n):
    graph[i] = list(map(int, str(input().rstrip())))
visited = [[0]*m for _ in range(n)]
# pprint(visited)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(i, j):
    global cnt
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1

    while queue:
        # pprint(visited)
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                # if nx == n-1 and ny == m-1:
                #     break
                if visited[nx][ny] == 0 and graph[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))

bfs(0, 0)
print(visited[n-1][m-1])