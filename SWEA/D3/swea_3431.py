# import sys

# sys.stdin = open("swea_3431_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    l, u, x = map(int, input().split())

    if x < l:
        answer = l - x
    elif l <= x <= u:
        answer = 0
    else:
        answer = -1
    print(f"#{tc} {answer}")
