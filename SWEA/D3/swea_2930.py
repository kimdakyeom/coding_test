import sys
sys.stdin = open("swea_2930_input.txt", "r")

import heapq

for tc in range(1, int(input()) + 1):
    answer = []
    n = int(input())
    heap = []
    for _ in range(n):
        num = list(map(int, input().split()))
        if num[0] == 1:
            heap.append(num[1])
        else:
            max_heap = []
            for item in heap:
                heapq.heappush(max_heap, (-item, item))
            if len(heap) == 0:
                answer.append(-1)
            else:
                max_item = heapq.heappop(max_heap)[1]
                answer.append(max_item)
                heap.remove(max_item)
    print(f'#{tc}', end=" ")
    print(*answer)
