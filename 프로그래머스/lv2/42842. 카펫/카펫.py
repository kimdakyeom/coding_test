def solution(brown, yellow):
    answer = []

    for i in range(1, 10000):
        for j in range(1, 10000):
            if (i * j) == (brown + yellow) and ((i * 2 )+ (j * 2) - 4) == brown:
                answer = [i, j]
    return answer