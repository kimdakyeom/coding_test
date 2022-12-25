import sys

input = sys.stdin.readline

r, c = map(int, input().split())
board = []
for _ in range(r):
    board.append(list(input().rstrip()))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs(x, y):
    w, s = 0, 0
    queue = [(x,y)]

    while queue:
        x, y = queue.pop()

        if board[x][y] == 'v':
            w += 1
        if board[x][y] == 'o':
            s += 1
        board[x][y] = '#'

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c and board[nx][ny] != '#':
                queue.append((nx, ny))
    if s <= w:
        s = 0
    else:
        w = 0
    return s, w

wCnt = 0
sCnt = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'v' or board[i][j] == 'o':
            w, s = bfs(i, j)
            wCnt += w
            sCnt += s
print(wCnt, sCnt)