import sys
input = sys.stdin.readline
from collections import deque
from pprint import pprint

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs():
    mqueue = deque()
    fqueue = deque()
    for i in range(r):
        for j in range(c):
            if miro[i][j] == 'J':
                if i == 0 or i == r - 1 or j == 0 or j == c - 1:
                    return 1
                mqueue.append((i, j))
            elif miro[i][j] == 'F':
                fqueue.append((i, j))
    cnt = 2
    while mqueue:
        for _ in range(len(fqueue)):
            x, y = fqueue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and (miro[nx][ny] == 'J' or miro[nx][ny] == '.'):
                    miro[nx][ny] = 'F'
                    fqueue.append((nx, ny))
        for _ in range(len(mqueue)):
            x, y = mqueue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < r and 0 <= ny < c and (miro[nx][ny] == '.'):
                    if nx == 0 or nx == r - 1 or ny == 0 or ny == c - 1:
                        return cnt
                    miro[nx][ny] = 'J'
                    mqueue.append((nx, ny))
        cnt += 1
    return "IMPOSSIBLE"


r, c = map(int, input().split())
miro = []

for i in range(r):
    miro.append(list(input().rstrip()))

print(bfs())