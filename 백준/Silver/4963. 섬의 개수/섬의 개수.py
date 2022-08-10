import sys
read = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(x, y):
    if 0 <= x < h and 0 <= y < w:
        if earth[x][y] == 1:
            earth[x][y] = 2
            dfs(x-1, y-1)
            dfs(x-1, y)
            dfs(x-1, y+1)
            dfs(x, y-1)
            dfs(x, y+1)
            dfs(x+1, y-1)
            dfs(x+1, y)
            dfs(x+1, y+1)
            return True
        return False

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    cnt = 0
    earth = []

    for i in range(h):
        earth.append(list(map(int, read().split())))
    for i in range(h):
        for j in range(w):
            if earth[i][j] == 1:
                dfs(i, j)
                cnt += 1
    print(cnt)