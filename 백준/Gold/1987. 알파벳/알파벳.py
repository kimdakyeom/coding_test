import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(x, y):
    global ans
    queue = set()
    cnt = 1
    queue.add((x, y, cnt, arr[0][0]))
    while queue:
        x, y, cnt, al_list = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] not in al_list:
                queue.add((nx, ny, cnt + 1, al_list + arr[nx][ny]))
                ans = max(ans, cnt + 1)
    print(ans)

r, c = map(int, input().split())
arr = []
ans = 1

for _ in range(r):
    arr.append(list(input().rstrip()))
bfs(0, 0)