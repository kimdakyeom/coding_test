# import sys
# sys.stdin = open("swea_2001_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    n, m = map(int, input().split())

    arr = [0 for _ in range(n)]
    sum_list = []

    for i in range(n):    
        arr[i] = list(map(int, input().split()))

    for i in range(n-m+1):
        for j in range(n-m+1):
            sum = 0
            for k in range(m):
                for l in range(m):
                    sum += arr[i+k][j+l]
            sum_list.append(sum)

    print(f'#{t} {max(sum_list)}')