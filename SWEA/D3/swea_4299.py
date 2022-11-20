# from pprint import pprint
# import sys
# sys.stdin = open("swea_4299_input.txt", 'rt', encoding='UTF8')

for tc in range(1, int(input())+1):
    d, h, m = map(int, input().split())
    answer = 0
    answer += m - 11
    answer += (h-11) * 60
    answer += (d-11) * 24 * 60

    if answer < 0:
        answer = -1
    print(f'#{tc} {answer}')