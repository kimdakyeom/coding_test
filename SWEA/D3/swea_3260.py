# import sys

# sys.stdin = open("swea_3260_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print(f"#{tc} {a+b}")
