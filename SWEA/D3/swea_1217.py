# import sys
# sys.stdin = open("swea_1217_input.txt", 'rt', encoding='UTF8')

def pow(n, m):
    if m == 0:
        return 1
    else:
        return pow(n, m-1) * n

t = 10

for T in range(1, t+1):
    test = int(input())
    n, m = map(int, input().split())

    print(f'#{test} {pow(n, m)}')