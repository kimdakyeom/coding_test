from pprint import pprint
import sys
sys.stdin = open("swea_4047_input.txt", 'rt', encoding='UTF8')

t = int(input())

for tc in range(1, t + 1) :
    board = [13] * 4
    data = input()

    visited = []

    for i in range(0, len(data), 3) :
        if data[i] == 'S' :
            board[0] -= 1
        elif data[i] == 'D' :
            board[1] -= 1
        elif data[i] == 'H' :
            board[2] -= 1
        else :
            board[3] -= 1
        if data[i:i+3] in visited :
            board = 'ERROR'
            break
        visited.append(data[i:i+3])

    if board == 'ERROR' :
        print(f'#{tc} {board}')
    else :
        print(f'#{tc}', *board)