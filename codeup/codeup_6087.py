n = int(input())

for num in range(1, n+1):
    if(num % 3 == 0):
        continue
    else:
        print(num, end=' ')