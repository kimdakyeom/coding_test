n, m = map(int, input().split())

maze = [list(input()) for _ in range(n)]

# 아래, 위, 왼, 오
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

queue = [[0, 0]]
maze[0][0] = 1

# queue가 1일때 반복
while queue:
    # a는 queue의 첫번째 값, b는 queue의 두번째 값
    a, b = queue[0][0], queue[0][1]
    # queue[0] 제거
    del queue[0]

    # 동서남북 검사
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        # x와 y가 판 안에 있고 값이 1이면
        if 0 <= x < n and 0 <= y < m and maze[x][y] == '1':
            # queue에 [x, y] 추가
            queue.append([x, y])

            # 기준이 되는 숫자에 +1
            maze[x][y] = maze[a][b] + 1
# 최솟값 출력
print(maze[n - 1][m - 1])