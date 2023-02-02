import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
friend = []
for i in range(n):
    friend.append(list(input()))

graph = [[0 for _ in range(n)] for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if friend[i][j] == 'Y' or (friend[i][k] == 'Y' and friend[k][j] == 'Y'):
                graph[i][j] = 1
answer = 0
for i in graph:
    answer = max(sum(i), answer)
print(answer)