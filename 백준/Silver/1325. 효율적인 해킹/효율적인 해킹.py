import sys
input = sys.stdin.readline
from collections import deque

def bfs(com):
    cnt = 0
    queue = deque([com])
    visited = [0 for _ in range(n+1)]
    visited[com] = 1
    while queue:
        tmp = queue.popleft()
        cnt += 1
        for i in graph[tmp]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
    return cnt

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)
max_ = 0
answer = [0 for _ in range(n+1)]
for i in range(1, n+1):
    answer[i] = bfs(i)
for i in range(1, n+1):
    if answer[i] == max(answer):
        print(i, end=' ')