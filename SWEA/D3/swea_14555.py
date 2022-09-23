# import sys
# sys.stdin = open("swea_14555_input.txt", "r")

n = int(input())

for tc in range(1, n + 1):
    soccer = input()
    cnt = 0
    for i in range(len(soccer) - 1):
        if soccer[i] == "(" and soccer[i+1] == ")":
            cnt += 1
        elif soccer[i] == "(" and soccer[i+1] == "|":
            cnt += 1
        elif soccer[i] == "|" and soccer[i+1] == ")":
            cnt += 1
    print(f'#{tc} {cnt}')