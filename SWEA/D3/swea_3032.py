# import sys
# sys.stdin = open("swea_3032_input.txt", 'rt', encoding='UTF8')

# 확장된 유클리드 알고리즘
def gcd(a, b):
    x, y, u, v = 0, 1, 1, 0
    while a != 0:
        q, r = b // a, b % a
        m, n = x - u * q , y - v * q
        b, a, x, y, u, v = a, r, u, v, m, n
    return [x, y]

for tc in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    print(f"#{tc} {' '.join(map(str, gcd(a, b)))}")