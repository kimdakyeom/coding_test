# import sys
# sys.stdin = open("swea_1220_input.txt", 'rt', encoding='UTF8')

for t in range(1, 11):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    deadlock = 0

    for i in range(n):
        flag = 0
        for j in range(n):
            if board[j][i] == 1:
                flag = 1
            elif board[j][i] == 2:
                if flag:
                    deadlock += 1
                    flag = 0

    print(f'#{t} {deadlock}')