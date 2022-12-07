import sys
# sys.stdin = open("input2.txt", "r")

from collections import Counter
n, m, inven = map(int, sys.stdin.readline().split())
ground = []
for _ in range(n): ground += map(int, sys.stdin.readline().split())

min_h = min(ground)
max_h = max(ground)
_sum = sum(ground)
height, max_time = 0, 1e8
ground = dict(Counter(ground))

for i in range(min_h, max_h+1):
    if _sum + inven >= i * n * m:
        _time = 0
        for key in ground:
            if key > i:
                _time += (key - i) * ground[key] * 2
            elif key < i:
                _time += (i - key) * ground[key]
        if _time <= max_time:
            max_time = _time
            height = i
print(max_time, height)