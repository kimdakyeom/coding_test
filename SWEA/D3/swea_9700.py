# import sys

# sys.stdin = open("swea_9700_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    p, q = map(float, input().split())
    # 1번 뒤집었을 때 USB가 꽂힐 확률
    # 처음에 뒤집어서 꽂고 다음에 제대로 꽂음
    s1 = (1 - p) * q
    # 2번 뒤집었을 때 USB가 꽂힐 확률
    # 처음에 올바른 면 & 비정상 꽂기, 그 다음 뒤집은 면, 마지막 제대로 꽂기
    s2 = p * (1 - q) * q
    if s2 > s1:
        print(f"#{tc} YES")
    else:
        print(f"#{tc} NO")
