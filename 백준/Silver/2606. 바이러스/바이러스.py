n = int(input())
m = int(input())

visited = [0] * (n+1)
graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
answer = 0
def dfs(v):
    global answer
    visited[v] = 1
    for i in range(1, n+1):
        if visited[i] == 0 and graph[v][i] == 1:
            answer += 1
            dfs(i)
dfs(1)
print(answer)