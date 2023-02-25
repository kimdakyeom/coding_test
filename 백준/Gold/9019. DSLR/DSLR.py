import sys
input = sys.stdin.readline
from collections import deque
from pprint import pprint

n = int(input())

def D(n):
    res = (n * 2) % 10000
    return res

def S(n):
    res = (n - 1) % 10000
    return res

def L(n):
    res = (10 * n + (n // 1000)) % 10000
    return res

def R(n):
    res = (n // 10 + (n % 10) * 1000) % 10000
    return res

def bfs(a, b):
    queue = deque()
    queue.append((a, ""))
    visited = set()
    visited.add(a)
    while queue:
        x, op = queue.popleft()
        if x == b:
            print(op)
            return
        tmp = D(x)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, op+"D"))
        tmp = S(x)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, op+"S"))
        tmp = L(x)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, op+"L"))
        tmp = R(x)
        if tmp not in visited:
            visited.add(tmp)
            queue.append((tmp, op+"R"))

for i in range(n):
    a, b = map(int, input().split())
    bfs(a, b)