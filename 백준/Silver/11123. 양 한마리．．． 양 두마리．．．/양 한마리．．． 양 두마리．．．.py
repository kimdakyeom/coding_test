from collections import deque
n = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    grid[y][x] = '.'
    while queue:
        y, x = queue.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == '#':
                queue.append((ny, nx))
                grid[ny][nx] = '.'

for _ in range(n):
    h, w = map(int, input().split())
    grid = []
    cnt = 0
    for i in range(h):
        grid.append(list(input()))
    for i in range(h):
        for j in range(w):
            if grid[i][j] == '#':
                bfs(i, j)
                cnt += 1
    print(cnt)