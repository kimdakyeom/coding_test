# from pprint import pprint
# import sys
# sys.stdin = open("swea_3809_input.txt", 'rt', encoding='UTF8')

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    num_str = ""
    while True:
        num_str += ''.join(map(str, input().split()))
        if len(num_str) == n:
            break
    d = 0
    answer = 0
    while True:
        if str(d) not in num_str:
            answer = d
            break
        d += 1
    print(f"#{tc} {answer}")