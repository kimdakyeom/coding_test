# import sys
# sys.stdin = open("swea_2005_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n = int(input())

    arr = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(n):
            if j == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{t}')

    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                print(arr[i][j], end=' ')
        print()