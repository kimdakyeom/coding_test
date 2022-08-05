def rev(n):
    return int(str(n)[::-1])

x, y = map(int, input().split())
x_rev = rev(x)
y_rev = rev(y)
sum = x_rev + y_rev

print(rev(sum))