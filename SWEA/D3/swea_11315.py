# import sys
# sys.stdin = open("swea_11315_input.txt", 'rt', encoding='UTF8')

def dfs(board):
    # 오른쪽, 아래, 우하, 좌하
    dx = [0, 1, 1, 1]
    dy = [1, 0, 1, -1]
    
    # board의 요소에 접근
    for i in range(n):
        for j in range(n):
            # board 요소가 'o'이면
            if board[i][j] == 'o':
                # 네 방향 확인
                for dir in range(4):
                    # 현재 값 넣기
                    nx = i
                    ny = j
                    cnt = 0

                    # 현재 값이 nXn 안에 있고, 'o'이면
                    while 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 'o':
                        # 갯수에 1 추가
                        cnt += 1
                        # 다음 방향으로 변경
                        nx += dx[dir]
                        ny += dy[dir]
                    # 다섯개 이상 연속이면
                    if cnt >= 5:
                        return 'YES'
    return 'NO'

for tc in range(1, int(input()) + 1):
    n = int(input())
    board = [input() for _ in range(n)]

    print(f'#{tc} {dfs(board)}')