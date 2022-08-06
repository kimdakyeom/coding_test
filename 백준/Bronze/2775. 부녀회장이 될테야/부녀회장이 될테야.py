T = int(input())

for t in range(1, T+1):
    k = int(input())
    n = int(input())

    arr = [list([0] * n) for _ in range(k+1)]

    for i in range(n):
        arr[0][i] = i+1

    for i in range(1, k+1):
        for j in range(n):
            arr[i][j] = arr[i][j-1] + arr[i-1][j]

    print(arr[k][n-1])