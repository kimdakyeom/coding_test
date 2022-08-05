a, b = map(int, input().split())

a = str(a)
b = str(b)

a_r = int(a[::-1])
b_r = int(b[::-1])

if a_r > b_r:
    print(a_r)
elif b_r > a_r:
    print(b_r)