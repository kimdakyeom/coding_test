import sys
input = sys.stdin.readline
from itertools import combinations

n, m = map(int, input().split())

list_ = [i for i in range(1, n+1)]
for i in combinations(list_, m):
    print(*i)