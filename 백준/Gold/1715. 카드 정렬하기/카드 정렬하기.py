import sys
from pprint import pprint
input = sys.stdin.readline
import heapq

n = int(input())
nums = []
answer = 0

for i in range(n):
    heapq.heappush(nums, int(input()))

while len(nums) != 1:
    n1 = heapq.heappop(nums)
    n2 = heapq.heappop(nums)
    tmp = n1 + n2
    answer += tmp
    heapq.heappush(nums, tmp)
print(answer)