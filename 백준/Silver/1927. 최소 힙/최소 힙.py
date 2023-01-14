import sys
input = sys.stdin.readline
import heapq

n = int(input())
heap = []

for i in range(n):
    a = int(input())
    if a != 0:
        heapq.heappush(heap, a)
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))