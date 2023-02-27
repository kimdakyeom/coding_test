import sys
input = sys.stdin.readline
import copy

n = int(input())
lines = []
ans = 0

for i in range(n):
    start, end = map(int, input().split())
    lines.append((start, end))
lines.sort()

min_, max_ = lines[0][0], lines[0][1]
for x, y in lines:
    if max_ < x:
        ans += max_ - min_
        min_, max_ = x, y
    max_ = max(max_, y)
ans += max_ - min_
print(ans)