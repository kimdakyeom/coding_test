import sys
input = sys.stdin.readline
from collections import deque

dx = [0,0,1,-1]
dy = [1,-1,0,0]

n, l, r = map(int, input().split())
arr = []
for i in range(n):
        arr.append(list(map(int, input().split())))

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    group = [(y, x)]
    while queue:
        y, x = queue.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny < n and 0 <= nx < n and l <= abs(arr[ny][nx] - arr[y][x]) <= r and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                queue.append((ny, nx))
                group.append((ny, nx))
    return group

answer = 0
while True:
    visited = [[0] * (n+1) for _ in range(n+1)]
    flag = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                visited[i][j] = 1
                group = bfs(i, j)
                if len(group) > 1:
                    flag = 1
                    number = sum([arr[x][y] for x, y in group]) // len(group)
                    for x, y in group:
                        arr[x][y] = number
    if flag == 0:
        break
    answer += 1
print(answer)