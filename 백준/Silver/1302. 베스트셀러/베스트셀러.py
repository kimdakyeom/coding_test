n = int(input())

books = []
board = {}

for i in range(n):
    title = input()
    books.append(title)

for i in books:
    if i in board:
        board[i] += 1
    else:
        board[i] = 1

book = [k for k, v in board.items() if max(board.values()) == v]
if len(book) >= 2:
    book.sort()
    print(book[0])
else:
    print(*book)