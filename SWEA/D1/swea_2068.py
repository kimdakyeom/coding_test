# import sys

# sys.stdin = open("swea_2068_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    num = list(map(int, input().split()))
    print(f'#{i} {max(num)}')