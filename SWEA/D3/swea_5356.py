# import sys
# sys.stdin = open("swea_5356_input.txt", 'rt', encoding='UTF8')

for t in range(1, int(input()) + 1):
    board = []
    for i in range(5):
        board.append(input())
    
    max_ = 0
    for i in board:
        if len(i) > max_:
            max_ = len(i)
    
    answer = ''
    for i in range(max_):
        for j in range(5):
            if i < len(board[j]):
                answer += board[j][i]
    
    print(f'#{t} {answer}')