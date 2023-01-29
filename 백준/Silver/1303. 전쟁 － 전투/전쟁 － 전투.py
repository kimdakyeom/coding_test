import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

war = []
for i in range(m):
    war.append(list(input().rstrip()))
visited = [[0] * n for _ in range(m)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(y, x, team):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    cnt = 0

    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nx < n and 0 <= ny < m and war[ny][nx] == team and not visited[ny][nx]:
                cnt += 1
                visited[ny][nx] = 1
                queue.append((ny, nx))
    return cnt + 1

ans_w = 0
ans_b = 0
for i in range(m):
    for j in range(n):
        if war[i][j] == 'W' and not visited[i][j]:
            ans_w += bfs(i, j, 'W') ** 2
        elif war[i][j] == 'B' and not visited[i][j]:
            ans_b += bfs(i, j, 'B') ** 2
print(ans_w, ans_b)