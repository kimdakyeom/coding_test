import sys
sys.stdin = open("swea_1215_input.txt", 'rt', encoding='UTF8')

def solve(y, x, length, wh):
    global answer
    result = ''
    if wh == 'w':
        for i in range(length):
            result += arr[y][x + i]
    else:
        for i in range(length):
            result += arr[y + i][x]
    
    yes = True

    for j in range(length // 2):
        if result[j] == result[-1 - j]:
            continue
        yes = False
        break
    if yes:
        answer += 1
    return

T = 10

for t in range(1, T+1):
    answer = 0
    n = int(input())
    arr = [input() for _ in range(8)]

    for i in range(0, 8):
        for j in range(9 - n):
            solve(i, j, n, 'w')
    for i in range(9 - n):
        for j in range(8):
            solve(i, j, n, 'h')
    
    print(f'#{t} {answer}')