n = int(input())

i = 1

while i <= n:
    if(i / 10 == 3 or i / 10 == 6 or i / 10 == 9):
        print("X", end=' ')
    if(i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
        print("X", end=' ')
    else:
        print(i, end=' ')
    i += 1