import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

draw = []
for i in range(n):
    draw.append(list(map(int, input().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(y, x):
    tmp_cnt = 0
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < n and 0 <= nx < m and draw[ny][nx] == 1:
                queue.append((ny, nx))
                draw[ny][nx] = 2
                tmp_cnt += 1
    if tmp_cnt == 0:
        tmp_cnt = 1
    return tmp_cnt

cnt = 0
size = 0
draw_size = 0
for i in range(n):
    for j in range(m):
        if draw[i][j] == 1:
            cnt += 1
            draw_size = max(draw_size, bfs(i, j))
print(cnt)
print(draw_size)