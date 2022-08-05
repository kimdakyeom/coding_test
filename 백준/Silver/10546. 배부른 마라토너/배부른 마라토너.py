from sys import stdin

n = int(stdin.readline())
dict = {}

for i in range(n):
    name = stdin.readline()
    if name in dict:
        dict[name] += 1
    else:
        dict[name] = 1

for i in range(n-1):
    name = stdin.readline()
    if dict[name] == 1:
        del dict[name]
    elif name in dict:
        dict[name] -= 1
print(*dict)