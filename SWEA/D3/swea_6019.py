# import sys

# sys.stdin = open("swea_6019_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    d, a, b, f = map(int, input().split())
    print(f'#{tc} {d / (a + b) * f}')