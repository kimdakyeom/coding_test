# import sys

# sys.stdin = open("swea_10200_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n, a, b = map(int, input().split())

    if a + b > n:
        print(f"#{tc} {min(a, b)} {a+b-n}")
    else:
        print(f"#{tc} {min(a, b)} 0")
