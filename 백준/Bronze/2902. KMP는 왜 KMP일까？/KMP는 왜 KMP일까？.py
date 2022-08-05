name = input()

for i in name:
    ascii = ord(i)
    if ascii >= 65 and ascii <= 90:
        print(i, end='')