# import sys
# sys.stdin = open("swea_12368_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    a, b = map(int, input().split())
    print(f'#{t} {(a+b)%24}')