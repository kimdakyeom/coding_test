import sys
input = sys.stdin.readline
import heapq

n = int(input())
schedule = []
heap = []
for i in range(n):
    start, end = map(int, input().split())
    schedule.append((start, end))
schedule.sort()

for s, e in schedule:
    if heap and heap[0] <= s:
        heapq.heappop(heap)
    heapq.heappush(heap, e)
print(len(heap))