import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())

answer = 0
visited = [0] * (f+1)
visited[0] = 1
cnt = 0

def bfs():
    global cnt
    queue = deque()
    queue.append((s, cnt))
    while queue:
        n, cnt = queue.popleft()
        if n == g:
            return cnt
        for i in [n+u, n-d]:
            if 0 < i <= f and visited[i] == 0:
                visited[i] = 1
                queue.append((i, cnt + 1))
    return "use the stairs"
answer = bfs()
print(answer)