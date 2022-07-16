n = int(input())

for i in range(n):
    st = input().split(" ")
    for word in st[1]:
        for i in word:
            print(i * int(st[0]), end='')
    print()