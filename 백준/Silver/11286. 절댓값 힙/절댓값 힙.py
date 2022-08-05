import heapq
import sys

input = sys.stdin.readline

heap = []

n = int(input())

for i in range(n):
    input_ = int(input())

    if input_ != 0:
        heapq.heappush(heap, (abs(input_), input_))
    else:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])