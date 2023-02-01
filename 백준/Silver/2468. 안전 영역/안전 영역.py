import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
area = []

for _ in range(n):
    area.append(list(map(int, input().split())))

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(y, x, k):
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < n:
                if area[ny][nx] > k and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append((ny, nx))

answer = 0
max_area = 0
for i in range(n):
    for j in range(n):
        if area[i][j] > max_area:
            max_area = area[i][j]

max_ = 0
for k in range(max_area):
    visited = [[0] * n for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(n):
            if area[i][j] > k and visited[i][j] == 0:
                bfs(i, j, k)
                answer += 1
    if max_ < answer:
        max_ = answer
print(max_)