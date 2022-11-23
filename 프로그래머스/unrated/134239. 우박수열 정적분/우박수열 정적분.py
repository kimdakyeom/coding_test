def collatz(k):
    k_list = [k]
    while k != 1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        k_list.append(k)
    return k_list

def solution(k, ranges):
    k_list = collatz(k)
    answer = []
    for a, b in ranges:
        c = len(k_list) + b - 1
        if a > c:
            answer.append(-1)
        else:
            sum_ = 0
            for i in range(a, c):
                sum_ += (k_list[i] + k_list[i+1]) / 2
            answer.append(sum_)
    return answer