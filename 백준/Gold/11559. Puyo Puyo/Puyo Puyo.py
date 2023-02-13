import sys
input = sys.stdin.readline
from collections import deque
from pprint import pprint

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs(x, y, c):
    queue = deque()
    queue.append((x, y))
    pang = deque()
    pang.append((x, y))
    visited = [[0] * 6 for _ in range(12)]
    visited[x][y] = 1
    cnt = 1
    flag = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 12 and 0 <= ny < 6 and visited[nx][ny] == 0 and puyo[nx][ny] == c:
                queue.append((nx, ny))
                pang.append((nx, ny))
                visited[nx][ny] = 1
                cnt += 1
    if cnt >= 4:
        flag = 1
        for x, y in pang:
            puyo[x][y] = '.'
    return flag

def gravity():
    for y in range(6):
        queue = deque()
        for x in range(11, -1, -1):
            if puyo[x][y] != '.':
                queue.append(puyo[x][y])
        for x in range(11, -1, -1):
            if queue:
                puyo[x][y] = queue.popleft()
            else:
                puyo[x][y] = '.'
puyo = []

for i in range(12):
    puyo.append(list(input().rstrip()))
answer = 0
while True:
    cnt = 0
    for i in range(12):
        for j in range(6):
            if puyo[i][j] != '.':
                cnt += bfs(i, j, puyo[i][j])
    if cnt == 0:
        print(answer)
        break
    else:
        answer += 1
    gravity()