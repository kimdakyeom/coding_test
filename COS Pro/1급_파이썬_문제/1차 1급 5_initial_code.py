#You may use import as below.
#import math

def solution(n):
    arr = [[0] * n for _ in range(n)]

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    x, y = 0, -1
    cnt = 1
    dir = 0

    while cnt <= n * n:
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
            arr[nx][ny] = cnt
            cnt += 1
            x, y = nx, ny
        else:
            dir = (dir + 1) % 4

    answer = 0
    
    for i in range(n):
        for j in range(n):
            if i == j:
                answer += arr[i][j]
    
    return answer


#The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret1, ".")
    
n2 = 2
ret2 = solution(n2)

#Press Run button to receive output. 
print("Solution: return value of the function is", ret2, ".")