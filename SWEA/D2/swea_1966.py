# import sys
# sys.stdin = open("swea_1966_input.txt", "r")

t = int(input())

for T in range(1, t+1):
    n = int(input())

    num = list(map(int, input().split()))
    num.sort()
    print(f'#{T}', end=' ')
    print(*num)