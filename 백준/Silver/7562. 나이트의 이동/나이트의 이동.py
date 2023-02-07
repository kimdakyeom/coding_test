import sys
input = sys.stdin.readline
from collections import deque

dy = [-1, -2, -2, -1, 1, 2, 2, 1]
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
def bfs(x, y, end_x, end_y):
    queue = deque()
    cnt = 0
    queue.append((x, y, cnt))
    visited[x][y] = 1
    while queue:
        x, y, cnt = queue.popleft()
        if x == end_x and y == end_y:
            print(cnt)
            break
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append((nx, ny, cnt + 1))

n = int(input())
for i in range(n):
    l = int(input().rstrip())
    board = [[0] * l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    visited = [[0] * l for _ in range(l)]
    end_x, end_y = map(int, input().split())
    bfs(start_x, start_y, end_x, end_y)