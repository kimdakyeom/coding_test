# import sys
# sys.stdin = open("swea_2805_input.txt", 'rt', encoding='UTF8')

T = int(input())

for t in range(1, T+1):
    n = int(input())
    farm = [list(map(int, input())) for _ in range(n)]

    ans = 0
    mid = n // 2
    start = n // 2
    end = n // 2

    for i in range(n):
        for j in range(start, end+1):
            ans += farm[i][j]
        
        if i < mid:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    print(f'#{t} {ans}')