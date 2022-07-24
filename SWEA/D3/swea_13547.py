# import sys
# sys.stdin = open("swea_13547_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    ox = input()
    cnt = 0
    
    for i in range(len(ox)):
        if ox[i] == 'x':
            cnt += 1
    if cnt >= 8:
        print(f'#{t} NO')
    else:
        print(f'#{t} YES')