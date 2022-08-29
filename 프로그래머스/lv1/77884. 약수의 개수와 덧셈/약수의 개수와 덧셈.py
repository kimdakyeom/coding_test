def solution(left, right):
    answer = 0

    for i in range(left, right + 1):
        su = []
        for j in range(1, i+1):
            if i % j == 0:
                su.append(j)
        if len(su) % 2 == 0:
            answer += su[-1]
        else:
            answer -= su[-1]
    
    return answer