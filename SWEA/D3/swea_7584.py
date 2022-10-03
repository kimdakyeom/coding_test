# import sys

# sys.stdin = open("swea_7584_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    k = int(input()) - 1

    # 1 이 되는 인덱스 : 2, 5, 6, 10, 11, 13, 14
    # 0 이 되는 인덱스 : 0, 1, 3, 4, 7, 8, 9, 12
    while 1:
        # 홀수면
        if k % 2 == 1:
            # 짝수가 될때까지 반복
            k -= 1
            k //= 2
        # 4의 배수
        elif k % 4 == 0:
            answer = 0
            break
        # 4의 배수가 아니면서 2의 배수
        else:
            answer = 1
            break
    print(f"#{tc} {answer}")
