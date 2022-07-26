# import sys
# sys.stdin = open("swea_1209_input.txt", "r")

T = 10

for t in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    result = []

    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[i][j]
        result.append(sum)

    for i in range(100):
        sum = 0
        for j in range(100):
            sum += arr[j][i]
        result.append(sum)

    sum = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                sum += arr[i][j]
    result.append(sum)

    sum = 0
    for i in range(100):
        arr[i] = arr[i][::-1]
    for i in range(100):
        for j in range(100):
            if i == j:
                sum += arr[i][j]
    result.append(sum)
    ans = max(result)

    print(f'#{t} {ans}')