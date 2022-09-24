# import sys
# sys.stdin = open("swea_11285_input.txt", "r", encoding='utf-8-sig')
import math

T = int(input())
ans_list = []

for tc in range(1, T + 1):
    n = int(input())
    ans = 0

    for _ in range(n):
        x, y = map(int, input().split())

        # 거리 계산 후 20으로 나누고 올림해서 점수의 인덱스 구하기
        num = math.ceil(math.sqrt((x ** 2) + (y ** 2)) / 20)

        # 인덱스가 0 이하이면 정가운데 쏜 것
        if num <= 0:
            # 10점 추가
            ans += 10
        # 인덱스가 11이하이면
        elif num <= 11:
            # 11에서 인덱스를 뺀 후 점수 추가
            ans += 11 - num

    ans_list.append("#%d %d" % (tc, ans))
for a in ans_list:
    print(a)