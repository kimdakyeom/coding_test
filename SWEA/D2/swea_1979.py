# import sys
# sys.stdin = open("swea_1979_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n, k = map(int, input().split())

    arr = [0 for _ in range(n)]

    for i in range(n):    
        arr[i] = list(map(int, input().split()))

    arr.insert(0, [0] * n)
    arr.insert(n+1, [0] * n)

    for i in range(n+2):
        arr[i].insert(0, 0)
        arr[i].insert(n+1, 0)

    cnt_list_w = []
    cnt_list_h = []
    ans = 0

    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j+1] == 0:
                cnt_list_w.append(cnt)
                cnt = 0

    for i in range(len(cnt_list_w)):
        if cnt_list_w[i] == k:
            ans += 1

    for i in range(1, n+1):
        cnt = 0
        for j in range(1, n+1):
            if arr[j][i] == 1:
                cnt += 1
            if arr[j+1][i] == 0:
                cnt_list_h.append(cnt)
                cnt = 0

    for i in range(len(cnt_list_h)):
        if cnt_list_h[i] == k:
            ans += 1
    print(f'#{t} {ans}')