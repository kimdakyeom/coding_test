import sys
input = sys.stdin.readline
from collections import deque
from pprint import pprint

n = int(input())

nums = list(map(int, input().split()))
nums.sort()
cnt = 0
for i in range(n):
    before_list = nums[0:i] + nums[i+1:]
    target = nums[i]
    start, end = 0, len(before_list) - 1
    while start < end:
        s = before_list[start] + before_list[end]
        if s == target:
            cnt += 1
            break
        elif s < target:
            start += 1
        elif s > target:
            end -= 1
print(cnt)