n = int(input())
hansu = 0

for i in range(1, n+1):
    l = list(map(int, str(i)))
    if i < 100:
        hansu += 1
    elif l[0] - l[1] == l[1] - l[2]:
        hansu += 1
print(hansu)

# 어려움..