# import sys

# sys.stdin = open("swea_9317_input.txt", "rt", encoding="UTF8")

for tc in range(1, int(input()) + 1):
    n = int(input())
    s_list = []
    s_list.append(input())
    s_list.append(input())
    answer = 0

    for i in range(n):
        if s_list[0][i] == s_list[1][i]:
            answer += 1
    print(f"#{tc} {answer}")
