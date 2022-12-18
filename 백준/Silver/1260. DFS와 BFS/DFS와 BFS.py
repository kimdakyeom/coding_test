n, m, v = map(int, input().split())

visited1 = [0] * (n+1)
visited2 = [0] * (n+1)

graph = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    u, w = map(int, input().split())
    graph[u][w] = graph[w][u] = 1

def dfs(v):
    visited1[v] = 1
    print(v, end=' ')
    for i in range(1, n+1):
        if visited1[i] == 0 and graph[v][i] == 1:
            dfs(i)

def bfs(v):
    queue = [v]
    visited2[v] = 1
    while queue:
        v = queue.pop(0)
        print(v, end=' ')
        for i in range(n+1):
            if visited2[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visited2[i] = 1
dfs(v)
print()
bfs(v)