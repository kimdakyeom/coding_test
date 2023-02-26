import sys
input = sys.stdin.readline
import copy

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
direction = [[], [[0], [1], [2], [3]], [[0, 1], [2, 3]], [[0, 2], [2, 1], [1, 3], [3, 0]],
             [[3, 0, 2], [1, 3, 0], [0, 2, 1], [2, 1, 3]], [[0, 1, 2, 3]]]

n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

def dfs(arr, depth):
    global ans
    if depth == len(cctv_list):
        ans = min(ans, sum([row.count(0) for row in arr]))
        return

    x, y = cctv_list[depth]
    for dirs in direction[arr[x][y]]:
        copy_arr = copy.deepcopy(arr)
        for dir in dirs:
            nx, ny = cctv_list[depth]
            while True:
                nx += dx[dir]
                ny += dy[dir]
                if not 0 <= nx < n or not 0 <= ny < m or copy_arr[nx][ny] == 6:
                    break
                if copy_arr[nx][ny] == 0:
                    copy_arr[nx][ny] = 7
        dfs(copy_arr, depth+1)
ans = 1e9
cctv_list = []

for i in range(n):
    for j in range(m):
        if arr[i][j] != 0 and arr[i][j] != 6:
            cctv_list.append((i, j))

dfs(arr, 0)
print(ans)