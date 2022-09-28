# import sys

# sys.stdin = open("swea_10726_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    # 이진수로 바꾸기
    binary = bin(m)[2:]
    cnt = 0

    # 뒤에서 n번째부터
    for i in binary[-n:]:
        # 1이면
        if i == "1":
            # 갯수 세기
            cnt += 1
    # 갯수가 n이면
    if cnt == n:
        print(f"#{tc} ON")
    else:
        print(f"#{tc} OFF")
