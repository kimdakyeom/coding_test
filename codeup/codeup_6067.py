n = int(input())

if n < 0:
    if n % 2 == 0:
        print("A")
    elif n % 2 == 1:
        print("B")
elif n > 0:
    if n % 2 == 0:
        print("C")
    elif n % 2 == 1:
        print("D")