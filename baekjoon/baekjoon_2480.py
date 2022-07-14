a, b, c = map(int, input().split(" "))
money = 0

if a == b == c:
    money = 10000 + a * 1000
elif a == b != c:
    money = 1000 + a * 100
elif a == c != b:
    money = 1000 + a * 100
elif b ==c != a:
    money = 1000 + b * 100
elif a != b != c:
    if a >= b >= c or a >= c >= b:
        money = a * 100
    elif b >= a >= c or b >= c >= a:
        money = b * 100
    elif c >= a >= b or c >= b >= a:
        money = c * 100
print(money)