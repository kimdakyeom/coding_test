# import sys

# sys.stdin = open("swea_3304_input.txt", "rt", encoding="UTF8")


def lcs(a, b):
    arr = [[0 for _ in range(len(b) + 2)] for _ in range(len(a) + 2)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            # a와 b 문자가 같으면
            if a[i - 1] == b[j - 1]:
                # 전 수에 1씩 증가
                arr[i][j] = arr[i - 1][j - 1] + 1
            # a와 b 문자가 다르면
            else:
                # 여태까지 셌던 횟수 넣기
                arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])
    # 두 문자열의 마지막 부분
    return arr[len(a)][len(b)]


for tc in range(1, int(input()) + 1):
    a, b = input().split()
    print(f"#{tc} {lcs(a, b)}")
