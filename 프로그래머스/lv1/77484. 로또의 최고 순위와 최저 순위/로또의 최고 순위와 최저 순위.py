def grade(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    elif num == 1:
        return 6
    elif num == 0:
        return 6

def solution(lottos, win_nums):
    answer = []
    ok = 0
    for lotto in lottos:
        if lotto in win_nums:
            ok = ok + 1
    first = ok + lottos.count(0)
    answer.append(grade(first))
    answer.append(grade(ok))
    return answer