import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []
time = []
for _ in range(n):
    s, t = map(int, input().split())
    time.append((s, t))
time.sort()
heapq.heappush(heap, time[0][1])
for i in range(1, n):
    if time[i][0] < heap[0]:
        heapq.heappush(heap, time[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, time[i][1])
print(len(heap))