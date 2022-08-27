from pprint import pprint
import sys
sys.stdin = open("swea_4615_input.txt", 'rt', encoding='UTF8')

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    length = int(n / 2)
    board[length-1][length-1] = 2
    board[length-1][length] = 1
    board[length][length-1] = 1
    board[length][length] = 2

    for i in range(m):
        x, y, color = map(int, input().split())
        board[y-1][x-1] = color

        dx = [1, -1, 0, 0, 1, 1, -1, -1]
        dy = [0, 0, 1, -1, 1, -1, 1, -1]
        now_dx, now_dy = y - 1, x - 1

        for dir in range(8):
            new_dx = now_dx + dx[dir]
            new_dy = now_dy + dy[dir]

            if new_dx >= n or new_dx < 0 or new_dy >= n or new_dy < 0:
                continue
            if board[new_dx][new_dy] != 0 and board[new_dx][new_dy] != board[now_dx][now_dy]:
                list_ = []
                while True:
                    new_new_dx = new_dx + dx[dir]
                    new_new_dy = new_dy + dy[dir]

                    if 0 <= new_new_dx < n and 0 <= new_new_dy < n:
                        if board[new_new_dx][new_new_dy] == 0:
                            list_ = []
                            break
                        elif board[new_new_dx][new_new_dy] != board[now_dx][now_dy]:
                            list_.append([new_dx, new_dy, board[now_dx][now_dy]])
                        elif board[new_new_dx][new_new_dy] == board[now_dx][now_dy]:
                            list_.append([new_dx, new_dy, board[now_dx][now_dy]])
                            break
                    else:
                        list_ = []
                        break
                    new_dx = new_new_dx
                    new_dy = new_new_dy
                
                if list_:
                    for k in list_:
                        board[k[0]][k[1]] = k[2]
    black, white = 0, 0
    for i in range(len(board)):
        black += board[i].count(1)
        white += board[i].count(2)
    
    print(f'#{t} {black} {white}')