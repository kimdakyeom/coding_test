T = int(input())

for t in range(1, T+1):
    n, a, b = map(int, input().split())

    ans = -1
    for r in range(1, n+1):
        c = 1
        while r * c <= n:
            fomula = a * abs(r - c) + b * (n - r * c)
            if ans == -1:
                ans = fomula
            else:
                ans = min(ans, fomula)
            c += 1
    print(f'#{t} {ans}')