import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
time = []
for _ in range(n):
    num, start, end = map(int, input().split())
    heapq.heappush(heap, [start, end])
start, end = heapq.heappop(heap)
heapq.heappush(time, end)

while heap:
    start, end = heapq.heappop(heap)
    if time[0] <= start:
        heapq.heappop(time)
    heapq.heappush(time, end)
print(len(time))