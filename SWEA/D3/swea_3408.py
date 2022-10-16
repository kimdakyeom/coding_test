# import sys

# sys.stdin = open("swea_3408_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n = int(input())
    print(f"#{tc} {n * (n + 1) // 2} {n ** 2} {n * (n + 1)}")
