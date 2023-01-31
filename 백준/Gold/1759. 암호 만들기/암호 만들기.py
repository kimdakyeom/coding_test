import sys
input = sys.stdin.readline
from itertools import combinations

l, c = map(int, input().split())
pw = list(input().rstrip().split())
pw.sort()

all_m = ['a', 'e', 'i', 'o', 'u']

for i in combinations(pw, l):
    m, j = 0, 0
    for c in i:
        if c in all_m:
            m += 1
        else:
            j += 1
    if m > 0 and j > 1:
        print("".join(i))