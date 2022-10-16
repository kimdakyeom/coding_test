# import sys

# sys.stdin = open("swea_3376_input.txt", "rt", encoding="UTF8")

T = int(input())
list_ = [int(input()) for i in range(T)]
# 100번째까지 한번에 구해놓고 해결
pado = [1, 1, 1]
for i in range(3, 101):
    pado.append(pado[i - 3] + pado[i - 2])

for tc in range(1, T + 1):
    print(f"#{tc} {pado[list_[tc-1] - 1]}")
