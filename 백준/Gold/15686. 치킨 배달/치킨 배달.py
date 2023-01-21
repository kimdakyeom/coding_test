import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())
chicken = []
house = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 2:
            chicken.append((i,j))
        elif tmp[j] == 1:
            house.append((i,j))
chickens = list(combinations(chicken, m))

def count(x, y, chicken):
    min_ = 2 * n
    for c in chicken:
        cx, cy = c
        min_ = min(abs(cx-x) + abs(cy-y), min_)
    return min_

def solution():
    answer = 2 * n * len(house)
    for c in chickens:
        tmp = 0
        for h in house:
            x, y = h
            tmp += count(x, y, c)
        if tmp < answer:
            answer = tmp
    return answer
print(solution())