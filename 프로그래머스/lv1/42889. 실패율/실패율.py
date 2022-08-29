def solution(N, stages):
    cal = {}
    all = len(stages)

    for i in range(1, N + 1):
        if all != 0:
            cal[i] = stages.count(i) / all
            all -= stages.count(i)
        else:
            cal[i] = 0
    
    return sorted(cal, key=lambda k: cal[k], reverse=True)