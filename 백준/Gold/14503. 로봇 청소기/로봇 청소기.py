import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = []

for i in range(n):
    arr.append(list(map(int, input().split())))
answer = 0
def dfs(y, x, d):
    global answer
    if arr[y][x]==0:
        answer+=1
        arr[y][x]=2
    for _ in range(4):
        nd=(d+3)%4
        ny=y+dy[nd]
        nx=x+dx[nd]
        if arr[ny][nx]==0:
            dfs(ny, nx, nd)
            return
        d=nd
    nd=(d+2)%4
    ny=y+dy[nd]
    nx=x+dx[nd]
    if arr[ny][nx]==1:
        return
    dfs(ny, nx, d)

dfs(r, c, d)
print(answer)