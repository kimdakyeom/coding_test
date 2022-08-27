# import sys
# sys.stdin = open("swea_6190_input.txt", 'rt', encoding='UTF8')

T = int(input())

def danjo(n):
    n = str(n)
    for i in range(len(n)-1):
        if n[i] > n[i+1]:
            return 0
    return 1

for t in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))
    max_ = 0

    for i in range(n-1):
        for j in range(i+1, n):
            number = a[i] * a[j]
            if danjo(number):
                max_ = max(number, max_)
        if max_ == 0:
            max_ = -1
    print(f'#{t} {max_}')