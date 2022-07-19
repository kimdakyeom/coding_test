# import sys

# sys.stdin = open("swea_2072_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    num = list(map(int, input().split()))
    sum = 0

    for j in num:
        if j % 2 == 1:
            sum += j
    print(f'#{i} {sum}')