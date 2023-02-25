import sys
input = sys.stdin.readline
from collections import deque
from pprint import pprint

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(i, j):
    queue = deque()
    queue.append((i, j))
    visited = [[0] * w for _ in range(h)]
    visited[i][j] = 1
    tmp = 0
    while queue:
        x, y = queue.popleft()
        flag = True
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))
                flag = False
        if flag:
            tmp = max(tmp, visited[x][y]-1)
    return tmp


h, w = map(int, input().split())
arr = []
answer = 0

for i in range(h):
    arr.append(list(input().rstrip()))

for i in range(h):
    for j in range(w):
        if arr[i][j] == 'L':
            temp = bfs(i, j)
            answer = max(temp, answer)
print(answer)