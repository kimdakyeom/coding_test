n = int(input())

for i in range(n):
    ox = list(input())
    cnt = 0
    ans = 0
    for j in ox:
        if j == "O":
            cnt += 1
            ans += cnt
        elif j == "X":
            cnt = 0
    print(ans)