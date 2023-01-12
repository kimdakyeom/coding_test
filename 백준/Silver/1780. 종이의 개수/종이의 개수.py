import sys
input = sys.stdin.readline

n = int(input())

arr = []
answer = [0, 0, 0]
for _ in range(n):
    arr.append(list(map(int, input().split())))

def recursion(n, r, c):
    now = arr[r][c]

    for i in range(r, r+n):
        for j in range(c, c+n):
            if arr[i][j] != now:
                recursion(n//3, r, c)
                recursion(n//3, r, c+n//3)
                recursion(n//3, r, c+2*(n//3))
                recursion(n//3, r+n//3, c)
                recursion(n//3, r+n//3, c+n//3)
                recursion(n//3, r+n//3, c+2*(n//3))
                recursion(n//3, r+2*(n//3), c)
                recursion(n//3, r+2*(n//3), c+n//3)
                recursion(n//3, r+2*(n//3), c+2*(n//3))
                return
    if now == -1:
        answer[0] += 1
    elif now == 0:
        answer[1] += 1
    else:
        answer[2] += 1
    return
recursion(n, 0, 0)

for a in answer:
    print(a)