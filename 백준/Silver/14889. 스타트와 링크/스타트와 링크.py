import sys
from pprint import pprint
input = sys.stdin.readline

def dfs(depth, idx):
    global answer
    if depth == n // 2:
        p1, p2 = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    p1 += arr[i][j]
                elif not visited[i] and not visited[j]:
                    p2 += arr[i][j]
        answer = min(answer, abs(p1-p2))
        return

    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

n = int(input())
arr = []
answer = 1e9

for _ in range(n):
    arr.append(list(map(int, input().split())))

visited = [0 for _ in range(n)]
dfs(0, 0)
print(answer)