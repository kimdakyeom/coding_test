from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    percolates[y][x] = 2
    while queue:
        y, x = queue.popleft()
        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]
            if 0 <= ny < m and 0 <= nx < n and percolates[ny][nx] == 0:
                queue.append((ny, nx))
                percolates[ny][nx] = 2

m, n = map(int, input().split())
percolates = []
for i in range(m):
    percolates.append(list(map(int, input())))
for i in range(n):
    if percolates[0][i] == 0:
        bfs(0, i)
if 2 in percolates[-1]:
    print("YES")
else:
    print("NO")