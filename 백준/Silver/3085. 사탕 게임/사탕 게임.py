import sys
input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(input().rstrip()))

def width(w):
    tmp = 1
    cnt = 0
    for i in range(1, n):
        if arr[w][i-1] == arr[w][i]:
            tmp += 1
        else:
            tmp = 1
        if tmp > cnt:
            cnt = tmp
    return cnt

def height(h):
    tmp = 1
    cnt = 0
    for i in range(1, n):
        if arr[i-1][h] == arr[i][h]:
            tmp += 1
        else:
            tmp = 1
        if tmp > cnt:
            cnt = tmp
    return cnt

answer = 0
tmp = 0
for i in range(n):
    for j in range(n):
        if j+1 < n:
            arr[i][j] , arr[i][j+1] = arr[i][j+1], arr[i][j]
            for k in range(n):
                tmp = width(k)
                if tmp > answer:
                    answer = tmp
            for k in range(n):
                tmp = height(k)
                if tmp > answer:
                    answer = tmp
            arr[i][j] , arr[i][j+1] = arr[i][j+1], arr[i][j]
        if i+1 < n:
            arr[i][j] , arr[i+1][j] = arr[i+1][j], arr[i][j]
            for k in range(n):
                tmp = width(k)
                if tmp > answer:
                    answer = tmp
            for k in range(n):
                tmp = height(k)
                if tmp > answer:
                    answer = tmp
            arr[i][j] , arr[i+1][j] = arr[i+1][j], arr[i][j]
print(answer)