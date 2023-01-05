import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        node = queue.popleft()
        for n in graph[node]:
            if visited[n] == 0:
                visited[n] = visited[node] + 1
                queue.append(n)

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
bfs(1)
print(visited.index(max(visited)), max(visited)-1, visited.count(max(visited)))