#You may use import as below.
#import math

def solution(pos):
    board = [[0] * 8 for _ in range(8)]
    dx = [-2, -1, 1, 2, -2, -1, 1, 2]
    dy = [-1, -2, -2, -1, 1, 2, 2, 1]

    x = ord(pos[0]) -65
    y = int(pos[1]) - 1
    cnt = 0
    dir = 0

    while dir < 8:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < 8 and 0 <= ny < 8:
            board[nx][ny] = 1
            cnt += 1
            dir += 1
        else:
            dir += 1

    return cnt

#The following is code to output testcase.
pos = "D4"
ret = solution(pos)

#Press Run button to receive output.
print("Solution: return value of the function is", ret, ".")