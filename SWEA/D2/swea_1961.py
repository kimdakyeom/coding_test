# import sys
# sys.stdin = open("swea_1961_input.txt", "r")

t = int(input())

for T in range(1, t+1):
    n = int(input())

    # 입력값을 반복문으로 받아온 후 리스트로 저장
    num = [list(map(int, input().split())) for i in range(n)]
    # n*n 배열에 0 집어넣기
    num_90 = [[0 for i in range(n)] for i in range(n)]
    num_180 = [[0 for i in range(n)] for i in range(n)]
    num_270 = [[0 for i in range(n)] for i in range(n)]
    
    # num을 90도 돌리기
    for i in range(n):
        for j in range(n):
            num_90[i][j] = num[n-1-j][i]

    # num_90을 90도 돌리기
    for i in range(n):
        for j in range(n):
            num_180[i][j] = num_90[n-1-j][i]

    # num_180을 90도 돌리기
    for i in range(n):
        for j in range(n):
            num_270[i][j] = num_180[n-1-j][i]

    print(f'#{T}')
    
    for i in range(n):
        # [0][0] [1][0] [2][0] ... 출력
        for a in range(n):
            print(num_90[i][a], end='')
        print(end=' ')
        # [0][1] [1][1] [2][1] ... 출력
        for b in range(n):
            print(num_180[i][b], end='')
        print(end=' ')
        # [0][2] [1][2] [2][2] ... 출력
        for c in range(n):
            print(num_270[i][c], end='')
        print()