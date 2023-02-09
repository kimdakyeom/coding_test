import sys
input = sys.stdin.readline
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def nor_bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and nor_visited[nx][ny] == 0 and color[x][y] == color[nx][ny]:
                queue.append((nx, ny))
                nor_visited[nx][ny] = 1

def abnor_bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and abnor_visited[nx][ny] == 0 and abcolor[x][y] == abcolor[nx][ny]:
                queue.append((nx, ny))
                abnor_visited[nx][ny] = 1

n = int(input())

color = []
for _ in range(n):
    color.append(list(input().rstrip()))

abcolor = []
for i in range(n):
    tmp = ''.join(color[i])
    tmp2 = tmp.replace('R', 'G')
    abcolor.append(list(tmp2))

nor_visited = [[0] * n for _ in range(n)]
abnor_visited = [[0] * n for _ in range(n)]
nor = 0
abnor = 0
ans = []
for i in range(n):
    for j in range(n):
        if nor_visited[i][j] == 0:
            nor_bfs(i, j)
            nor += 1
ans.append(nor)
for i in range(n):
    for j in range(n):
        if abnor_visited[i][j] == 0:
            abnor_bfs(i, j)
            abnor += 1
ans.append(abnor)
print(*ans)