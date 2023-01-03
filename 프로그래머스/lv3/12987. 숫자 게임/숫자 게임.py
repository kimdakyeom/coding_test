def solution(A, B):
    answer = 0
    A.sort(reverse=True)
    B.sort(reverse=True)
    for a in A:
        if B[0] > a:
            answer += 1
            del B[0]
    return answer