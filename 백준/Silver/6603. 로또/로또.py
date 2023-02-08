import sys
input = sys.stdin.readline
from collections import deque

def back(depth, i):
    if depth == 6:
        print(*answer)
        return
    for i in range(i, k):
        answer.append(lotto[i])
        back(depth + 1, i + 1)
        answer.pop()

while True:
    tmp = list(map(int, input().split()))
    k = tmp[0]
    if k == 0:
        break
    else:
        lotto = tmp[1:]
        answer = []
        back(0, 0)
    print()