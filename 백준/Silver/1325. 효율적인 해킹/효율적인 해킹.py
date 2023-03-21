import sys

from pprint import pprint
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def bfs(cur):
    global tmp_max
    q = deque([cur])
    visited[cur] = 1
    cnt = 0
    while q:
        c = q.popleft()
        cnt += 1
        for n in graph[c]:
            if not visited[n]:
                q.append(n)
                visited[n] = 1
    return cnt

answer = 0
answer_list = []
max_ = 0
for i in range(1, n+1):
    visited = [0] * (n+1)
    answer_list.append((i, bfs(i)))
answer_list.sort(key=lambda x : (-x[1], x[0]))
max_ = answer_list[0][1]

result = []
for a in answer_list:
    if a[1] == max_:
        result.append(a[0])
print(*result)