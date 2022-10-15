# import sys

# sys.stdin = open("swea_3142_input.txt", "rt", encoding="UTF8")

# 뿔이 2개와 1개이기 때문에
# 트윈혼 마릿수 = 총 마릿수 - 총 뿔 갯수
for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    print(f"#{tc} {m-(n-m)} {n-m}")
