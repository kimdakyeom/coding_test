# import sys
# sys.stdin = open("swea_12221_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    a, b = map(int, input().split())
    if a < 10 and b < 10:
        print(f'#{t} {a*b}')
    else:
        print(f'#{t} -1')