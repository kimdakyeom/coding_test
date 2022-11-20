# from pprint import pprint
# import sys
# sys.stdin = open("swea_4371_input.txt", 'rt', encoding='UTF8')

for tc in range(1, int(input())+1):
    n = int(input())
    days = []
    for i in range(n):
        days.append(int(input()))
    tmp = []
    for i in range(1, len(days)):
        if (days[i]-1) not in tmp:
            cnt = 0
            if tmp:
                for j in tmp:
                    if (days[i]-1) % j == 0:
                        cnt = 1
            if cnt == 0:
                tmp.append(days[i]-1)
    print(f'#{tc} {len(tmp)}')