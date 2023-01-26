import sys
input = sys.stdin.readline
from itertools import combinations

n = int(input())
nums = []

for i in range(1, 11):
    for c in combinations(range(0, 10), i):
        c = sorted(c, reverse=True)
        nums.append(int(''.join(map(str, c))))
nums.sort()

try:
    print(nums[n])
except:
    print(-1)