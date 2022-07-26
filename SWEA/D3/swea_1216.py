import sys
sys.stdin = open("swea_1216_input.txt", 'rt', encoding='UTF8')

def solve(y, x, wh):
    global answer
    result = ''
    length = 8

    while True:
        if wh == 'w':
            for i in range(length):
                result += arr[y][x + i]
                print(result)
            for j in range(length // 2):
                if result[j] == result[-1 - j]:
                    answer = len(result)
                    break
        else:
            for i in range(length):
                result += arr[y + i][x]
            for j in range(length // 2):
                if result[j] == result[-1 - j]:
                    answer = len(result)
                    break
        length -= 1
    return


for t in range(1, 11):
    n = int(input())
    arr = [input() for _ in range(8)]

    for i in range(0, 8):
        for j in range(9 - n):
            solve(i, j, 'w')
    for i in range(9 - n):
        for j in range(8):
            solve(i, j, 'h')
    
    print(f'#{t} {answer}')