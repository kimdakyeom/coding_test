import math
def solution(n, stations, w):
    answer = 0
    top = 2 * w + 1
    segments = []
    if stations[0] - w - 1 >= 1:
        segments.append([1, stations[0]-w-1])
    for i in range(len(stations)-1):
        start = stations[i] + w + 1
        end = stations[i+1] - w - 1
        if start <= end:
            segments.append([start, end])
    if stations[-1] + w + 1 <= n:
        segments.append([stations[-1]+w+1, n])
    
    for s in segments:
        diff = s[1] - s[0] + 1
        answer += math.ceil(diff / top)
    
    return answer