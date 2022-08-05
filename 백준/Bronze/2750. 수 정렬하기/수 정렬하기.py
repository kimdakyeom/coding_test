import heapq

n = int(input())
heap = []

for i in range(n):
    heap.append(int(input()))

for i in range(len(heap)):
    heapq.heapify(heap)
    print(heapq.heappop(heap))