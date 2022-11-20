import copy
from collections import deque
import sys


input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0
q = deque()


def bfs():
    global ans
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    w = copy.deepcopy(arr)
    for i in range(n):
        for j in range(m):
            if w[i][j] == 2:
                q.append([i, j])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if w[nx][ny] == 0:
                    w[nx][ny] = 2
                    q.append([nx, ny])
    cnt = 0
    for i in w:
        cnt += i.count(0)
    ans = max(ans, cnt)


def wall(x):
    if x == 3:
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(x + 1)
                arr[i][j] = 0


wall(0)
print(ans)
