import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K and len(scoville) != 1:
        answer += 1
        new = heapq.heappop(scoville) + (heapq.heappop(scoville) * 2)

        heapq.heappush(scoville, new)

    if scoville[0] < K:
        return -1
    else:
        return answer