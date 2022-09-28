# import sys

# sys.stdin = open("swea_10570_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    cnt = 0
    for num in range(a, b + 1):
        # 제곱근
        root = num ** (1 / 2)
        # 제곱근이 정수일때
        if root == int(root):
            # num을 문자열로
            num = str(num)
            # 제곱근을 문자열로
            root = str(int(root))
            # 현재 값과 제곱근이 모두 회문이면
            if num == num[::-1] and root == root[::-1]:
                cnt += 1
    print(f"#{tc} {cnt}")
