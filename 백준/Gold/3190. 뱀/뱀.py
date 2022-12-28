import sys
from collections import deque
input = sys.stdin.readline

def turn(a):
    global direct
    if a == 'L':
        direct = (direct - 1) % 4
    else:
        direct = (direct + 1) % 4

n = int(input())
k = int(input())

board = [[0] * (n) for _ in range(n)]

for i in range(k):
    a, b = map(int, input().split())
    board[a-1][b-1] = 2

l = int(input())

apple = {}
for i in range(l):
    x, d = input().split()
    apple[int(x)] = d

queue = deque()
queue.append((0,0))
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
x, y, cnt, direct = 0, 0, 0, 0

while True:
    x += dx[direct]
    y += dy[direct]
    cnt += 1

    if x < 0 or x >= n or y < 0 or y >= n:
        break
    if board[x][y] == 2:
        board[x][y] = 1
        queue.append((x,y))
        if cnt in apple:
            turn(apple[cnt])
    elif board[x][y] == 0:
        board[x][y] = 1
        queue.append((x,y))
        nx, ny = queue.popleft()
        board[nx][ny] = 0
        if cnt in apple:
            turn(apple[cnt])
    else:
        break
print(cnt)