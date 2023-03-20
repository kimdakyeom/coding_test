import sys
from pprint import pprint
input = sys.stdin.readline
from copy import deepcopy

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = 0
visited = [0]*2001

def dfs(cur, cnt):
    global answer
    visited[cur] = 1
    if cnt == 4:
        answer = 1
        return
    for node in graph[cur]:
        if visited[node] == 0:
            visited[node] = 1
            dfs(node, cnt+1)
            visited[node] = 0

for i in range(n):
    dfs(i, 0)
    visited[i] = 0
    if answer:
        break

print(answer)