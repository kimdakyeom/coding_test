# import sys
# sys.stdin = open("swea_4613_input.txt", 'rt', encoding='UTF8')

T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    flag = [list(input()) for _ in range(n)]
    min_ = n * m

    w_cnt = 0
    for w in range(0, n-2):
        for k in range(0, m):
            if flag[w][k] != 'W':
                w_cnt += 1
        
        b_cnt = 0
        for b in range(w+1, n-1):
            for k in range(0, m):
                if flag[b][k] != 'B':
                    b_cnt += 1
            
            r_cnt = 0
            for r in range(b+1, n):
                for k in range(0, m):
                    if flag[r][k] != 'R':
                        r_cnt += 1
            
            cnt = w_cnt + b_cnt + r_cnt
            if cnt < min_:
                min_ = cnt
    print(f'#{t} {min_}')