def solution(n):
    answer = 0
    d = 1

    while n > 0:
        if n % d == 0:
            answer += 1
        n -= d
        d += 1
    return answer