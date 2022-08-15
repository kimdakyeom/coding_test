# import sys
# sys.stdin = open("swea_2814_input.txt", 'rt', encoding='UTF8')

def dfs(i, cnt):
    global max_

    for j in range(1, n+1):
        if visited[j] == 0 and adj[i][j]:
            visited[j] = 1
            dfs(j, cnt+1)
            visited[j] = 0
        else:
            if cnt > max_:
                max_ = cnt

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    visited = [0] * (n+1)
    adj = [[0] * (n+1) for _ in range(n+1)]
    max_ = 0

    for i in range(m):
        x, y = map(int, input().split())
        adj[x][y] = 1
        adj[y][x] = 1
    
    for i in range(1, n+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    print(f'#{t} {max_}')