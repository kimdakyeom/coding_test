# import sys

# sys.stdin = open("swea_6692_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n = int(input())
    answer = 0

    for i in range(n):
        p, x = map(float, input().split())
        answer += p * x
    print(f"#{tc} {answer}")
