T = int(input())

for t in range(T):
    n, m = list(map(int, input().split()))
    cnt = 0
    for i in range(n, m+1):
        cnt += str(i).count('0')
    print(cnt)