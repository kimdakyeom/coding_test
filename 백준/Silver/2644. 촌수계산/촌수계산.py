import sys
input = sys.stdin.readline

def dfs(v):
    for i in graph[v]:
        if visited[i] == -1:
            visited[i] = visited[v] + 1
            dfs(i)

n = int(input())
A, B = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited[A] = 0
# A가 시작 노드
dfs(A)
print(visited[B])