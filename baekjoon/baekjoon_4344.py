c = int(input())

for i in range(c):
    n = list(map(int,input().split(" ")))
    avg = sum(n[1: ])/n[0]
    cnt = 0
    for j in range(1, n[0]+1):
        if n[j] > avg:
            cnt += 1
    print(f'{cnt / n[0] * 100:.3f}%')