import sys
input = sys.stdin.readline
from collections import deque
from pprint import pprint

t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int, input().split()))
    max_ = 0
    answer = 0
    for i in range(n-1, -1, -1):
        if nums[i] > max_:
            max_ = nums[i]
        else:
            answer += max_ - nums[i]
    print(answer)