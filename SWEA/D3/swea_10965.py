# import sys
# sys.stdin = open("swea_10965_input.txt", "r", encoding='UTF-8')

import math

ans_list = []

for tc in range(1, int(input() + 1)):
    a = int(input())
    i = 1

    while True:
        if math.sqrt(a * i) == int(math.sqrt(a * i)):
            ans_list.append(f'#{tc} {i}')
            break
        else:
            i += 1
print(ans_list)