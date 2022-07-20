# import sys
# sys.stdin = open("swea_1986_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    sum = 0
    num = int(input())
    for j in range(1, num+1):
        if j % 2 == 1:
            sum += j
        elif j % 2 == 0:
            sum -= j
    print(f'#{i} {sum}')