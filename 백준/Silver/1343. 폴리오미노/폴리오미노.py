board = input()
i = 0
answer = ''

while True:
    if board[i:i+4] == "XXXX":
        answer += "AAAA"
        i += 4
    elif board[i:i+2] == "XX":
        answer += "BB"
        i += 2
    elif board[i] == "X":
        answer = -1
        break
    else:
        answer += board[i]
        i += 1
    if i >= len(board):
        break
print(answer)