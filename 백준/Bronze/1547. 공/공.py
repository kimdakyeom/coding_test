n = int(input())

ans = 1

for tc in range(n):
    x, y = map(int, input().split())

    if x == ans:
        ans = y
    elif y == ans:
        ans = x
    else:
        continue
print(ans)