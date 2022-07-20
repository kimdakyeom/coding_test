# import sys
# sys.stdin = open("swea_1946_input.txt", "r")

t = int(input())

for i in range(1, t+1):
    n = int(input())
    list = []

    for j in range(1, n+1):
        alpha, num = input().split()
        sum = 0

        for k in range(1, int(num)+1):
            list.append(alpha)

    print(f'#{i}')
    idx = 0
    cnt = len(list) // 10 + 1
    
    for j in range(cnt):
        print(*list[idx:idx+10], sep='')
        idx += 10