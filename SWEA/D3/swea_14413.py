# import sys
# sys.stdin = open("swea_14413_input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [list(input()) for _ in range(n)]
    list_ = [0, 0, 0, 0]

    for i in range(n):
        for j in range(m):
            # arr에서 # 이면
            if arr[i][j] == '#':
                # 인덱스의 합이 짝수면
                if (i + j) % 2 == 0:
                    list_[0] += 1
                # 인덱스의 합이 홀수면
                elif (i + j) % 2 == 1:
                    list_[1] += 1
            # arr에서 .이면
            elif arr[i][j] == ".":
                # 인덱스의 합이 짝수면
                if (i + j) % 2 == 0:
                    list_[2] += 1
                # 인덱스의 합이 홀수면
                elif (i + j) % 2 == 1:
                    list_[3] += 1
    
    # list의 0, 1이 같이 존재하거나 0, 2이 같이 존재할 때, list의 2,3이 같이 존재하거나, 1,3이 같이 존재할때
    if (list_[0] and list_[1]) or (list_[2] and list_[3]) or (list_[0] and list_[2]) or (list_[1] and list_[3]):
        # impossible 출력
        answer = 'impossible'
    else:
        answer = 'possible'

    print(f'#{tc} {answer}')