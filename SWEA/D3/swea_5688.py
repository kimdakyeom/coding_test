import sys

sys.stdin = open("swea_5688_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n = int(input())
    # pow(n, 1/3) = 3.9999999996 이기때문에
    # 소수 두번째 자리에서 반올림
    num = round(pow(n, 1/3), 2)
    # 정수인지 판단
    if int(num) == num:
        print(f'#{tc} {int(num)}')
    else:
        print(f'#{tc} -1')