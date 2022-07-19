# import sys
# sys.stdin = open("swea_1284_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    p, q, r, s, w = list(map(int, input().split()))
    a = p * w
    if w <= r:
        b = q
    else:
        b = q + s * (w-r)
    if a < b:
        print(f'#{i} {a}')
    elif b < a:
        print(f'#{i} {b}')