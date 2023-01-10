import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

answer = 0
def recur(n, row, colum):
    global answer

    if row == r and colum == c:
        print(int(answer))
        exit(0)

    if n == 1:
        answer += 1
        return

    if row > r or row+n <= r or colum > c or colum+n <= c:
        answer += n**2
        return
    recur(n//2, row, colum)
    recur(n//2, row, colum+n/2)
    recur(n//2, row+n/2, colum)
    recur(n//2, row+n/2, colum+n/2)

print(recur(2**n, 0, 0))