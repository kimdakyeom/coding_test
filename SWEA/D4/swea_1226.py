import sys
sys.stdin = open("swea_1226_input.txt", 'rt', encoding='UTF8')

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for t in range(1, 11):
    answer = 0
    n = int(input())
    arr = [list(input()) for _ in range(16)]

    x, y = 0, 0
    for i in range(16):
        for j in range(16):
            if arr[i][j] == '2':
                x, y = i, j

    stack = [(x, y)]
    while stack:
        now_x, now_y = stack.pop()

        for dir in range(4):
            next_x = now_x + dx[dir]
            next_y = now_y + dy[dir]

            if 0 <= next_x < 16 and 0 <= next_y < 16:
                if arr[next_x][next_y] == '0':
                    stack.append((next_x, next_y))
                    arr[next_x][next_y] = '-1'
                elif arr[next_x][next_y] == '3':
                    answer = 1
                    stack.clear()
                    break
                
    print(f'#{t} {answer}')