# import sys
# sys.stdin = open("swea_1954_input.txt", "r")

t = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

for i in range(1, t+1):
    n = int(input())
    array = [[0] * n for _ in range(n)]
    r, c = 0, 0
    d = 0

    for j in range(1, n*n+1):
        array[r][c] = j
        r += dr[d]
        c += dc[d]

        if r < 0 or c < 0 or r >= n or c >= n or array[r][c] != 0:
            r -= dr[d]
            c -= dc[d]
            d = (d + 1) % 4

            r += dr[d]
            c += dc[d]

    print(f'#{i}')
    for j in array:
        print(*j)

# 어려워...