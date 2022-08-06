import sys
sys.stdin = open("swea_1216_input.txt")

for t in range(1, 11):
    tc = int(input())
    board = [list(input()) for _ in range(100)]

    def check(string, length):
        max_ = length
        while length <= 100:
            ans = 0
            for i in range(100):
                for j in range(101-length):
                    word = string[i][j:j+length]
                    if word == word[::-1]:
                        max_ = length
                        ans = 1
                        break
                if ans == 1:
                    break
            length += 1
        return max_

    row = check(board, 1)

    trans_board = [[0] * 100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            trans_board[i][j] = board[j][i]

    col = check(trans_board, 1)

    print(f'#{t} {max(row, col)}')