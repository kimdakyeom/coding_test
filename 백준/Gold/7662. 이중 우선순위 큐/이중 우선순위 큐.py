import sys
import heapq

input = sys.stdin.readline

t = int(input())

for i in range(t):
    k = int(input())
    heap = []
    max_heap = []
    visited = [False] * 1000001
    for key in range(k):
        tmp = input().split()
        command = tmp[0]
        n = int(tmp[1])
        if command == 'I':
            heapq.heappush(heap, (n, key))
            heapq.heappush(max_heap, (n*(-1), key))
            visited[key] = True
        else:
            if n == -1:
                while heap and not visited[heap[0][1]]:
                    heapq.heappop(heap)
                if heap:
                    visited[heap[0][1]] = False
                    heapq.heappop(heap)
            else:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while heap and not visited[heap[0][1]]:
        heapq.heappop(heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if heap and max_heap:
        print(-max_heap[0][0], heap[0][0])
    else:
        print('EMPTY')