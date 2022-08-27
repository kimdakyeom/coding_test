def solution(answers):
    first = [1, 2, 3, 4, 5]
    second = [2, 1, 2, 3, 2, 4, 2, 5]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer = [0] * 3
    for i in range(len(answers)):
        if first[i%5] == answers[i]:
            answer[0] += 1
        if second[i%8] == answers[i]:
            answer[1] += 1
        if third[i%10] == answers[i]:
            answer[2] += 1
    
    result = []
    for i in range(len(answer)):
        if answer[i] == max(answer):
            result.append(i+1)
    return result