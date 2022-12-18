n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
answer_list = []

def dfs(x, y):
    if 0 <= x <= n-1 and 0 <= y <= n-1 and arr[x][y] == 1:
        global count
        count += 1
        arr[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True
count = 0
answer = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            answer_list.append(count)
            answer += 1
            count = 0

answer_list.sort()
print(answer)

for i in range(len(answer_list)):
    print(answer_list[i])