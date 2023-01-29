import sys
input = sys.stdin.readline
from collections import deque

n = int(input())

graph = [[] for _ in range(n+1)]

while input:
    a, b = map(int, input().split())
    if a == -1 and b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

score = 0
count = 0
list_ = []

queue = deque()
def bfs(n):
    visited[n] = 1
    queue.append(n)
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
                dist[i] = dist[x] + 1

max_ = 1e8
cap = []
for i in range(1, len(graph)):
    visited = [0] * (n+1)
    dist = [0] * (n+1)
    bfs(i)
    max_d = max(dist)
    if max_d < max_:
        cap = [i]
        max_ = max_d
    elif max_d == max_:
        cap.append(i)
print(max_, len(cap))
print(*cap)