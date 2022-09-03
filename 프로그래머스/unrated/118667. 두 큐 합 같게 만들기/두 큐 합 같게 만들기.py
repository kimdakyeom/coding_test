from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1, queue2 = deque(queue1), deque(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)
    half_sum = (sum1 + sum2) // 2

    while queue1 and queue2:
        if sum1 > half_sum:
            sum1 -= queue1.popleft()
        elif sum1 < half_sum:
            pop_ = queue2.popleft()
            queue1.append(pop_)
            sum1 += queue1[-1]
        else:
            return answer
        answer += 1
    return -1