# import sys
# sys.stdin = open("swea_14692_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    if n % 2 == 0:
        print(f'#{tc} Alice')
    else:
        print(f'#{tc} Bob')