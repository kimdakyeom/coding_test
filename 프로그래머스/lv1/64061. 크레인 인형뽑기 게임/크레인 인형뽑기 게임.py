def solution(board, moves):
    answer = 0
    basket = []
    cnt = 0

    for i in range(len(moves)):
        for j in range(len(board)):
            if board[j][moves[i] - 1] != 0:
                basket.append(board[j][moves[i] - 1])
                if len(basket) >= 2:
                    if basket[-1] == basket[-2]:
                        basket.pop()
                        basket.pop()
                        cnt += 2
                board[j][moves[i] - 1] = 0
                break

    return cnt