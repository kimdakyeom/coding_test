import sys

input = sys.stdin.readline

s = [True] * (1000001)

for i in range(2, 1001):
    if s[i]:
        for j in range(i+i, 1000001, i):
            s[j] = False

while True:
    n = int(input())
    if n == 0:
        break
    for i in range(3, len(s)):
        if s[i] and s[n-i]:
            print(f'{n} = {i} + {n-i}')
            break
    else:
        print("Goldbach's conjecture is wrong.")