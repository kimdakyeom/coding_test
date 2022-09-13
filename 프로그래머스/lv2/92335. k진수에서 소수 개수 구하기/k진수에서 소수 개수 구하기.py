def solution(n, k):
    answer = ''
    result = 0

    while n:
        answer = str(n % k) + answer
        n //= k
    answer = answer.split("0")

    for i in answer:
        flag = True
        if len(i) > 0:
            for j in range(2, int(int(i) ** 0.5) + 1):
                if int(i) % j == 0:
                    flag = False
            if int(i) == 1:
                flag = False
            elif int(i) == 2:
                flag = True
            if flag == True:
                result += 1
    return result