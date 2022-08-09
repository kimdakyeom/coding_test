num = int(input())

for i in range(num+1):
    if all('4' == i or '7' == i for i in str(num - i)):
        print(str(num - i))
        break