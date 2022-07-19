# import sys

# sys.stdin = open("swea_2071_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    num = list(map(int, input().split()))
    sum = 0

    for j in num:
        sum += j
    avg = round(sum / 10)
    print(f'#{i} {avg}')