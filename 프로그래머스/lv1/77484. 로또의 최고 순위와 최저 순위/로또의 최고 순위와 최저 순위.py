def solution(lottos, win_nums):
    answer = []
    cnt = 0

    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            cnt += 1
    answer.append(cnt)

    for i in range(len(lottos)):
        if lottos[i] == 0:
            cnt += 1
    answer.append(cnt)

    for i in range(len(answer)):
        if answer[i] == 2:
            answer[i] = 5
        elif answer[i] == 3:
            answer[i] = 4
        elif answer[i] == 4:
            answer[i] = 3
        elif answer[i] == 5:
            answer[i] = 2
        elif answer[i] == 6:
            answer[i] = 1
        else:
            answer[i] = 6
    return sorted(answer)