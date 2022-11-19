from itertools import permutations
def solution(k, dungeons):
    answer = 0
    for permu in permutations(dungeons, len(dungeons)):
        temp_k = k
        cnt = 0
        for p in permu:
            if temp_k >= p[0]:
                temp_k -= p[1]
                cnt += 1
        answer = max(cnt, answer)
    return answer