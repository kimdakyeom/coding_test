import sys
from pprint import pprint
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[int(1e9)] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for i in range(r):
    u, v, t = map(int, input().split())
    graph[u][v] = t
    graph[v][u] = t

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for i in range(1, n+1):
    tmp = items[i-1]
    for j in range(1, n+1):
        if 0 < graph[i][j] <= m:
            tmp += items[j-1]
    if tmp > answer:
        answer = tmp
print(answer)