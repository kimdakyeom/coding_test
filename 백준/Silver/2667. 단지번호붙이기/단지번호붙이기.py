n = int(input())
arr = []

for i in range(n):
    tmp = []
    for j in list(map(str, input().strip())):
        tmp.append(int(j))
    arr.append(tmp)


def dfs(arr, i, j):
    stack = [[i, j]]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]
    result[cnt] = [[i, j]]

    while stack: 
        a, b = stack.pop()
        arr[a][b] = 0

        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0 <= x < n and 0 <= y < n and arr[x][y] == 1:
                result[cnt].append([x, y])
                arr[x][y] = 0
                stack.append([x, y])

cnt = 0
result = {}

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            cnt += 1
            dfs(arr, i, j)
            
print(len(result))

total = []

for i in result:
    total.append(len(result[i]))
total.sort()
for i in total:
    print(i)