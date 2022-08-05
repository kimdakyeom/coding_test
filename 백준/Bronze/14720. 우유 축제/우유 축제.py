import sys
input = sys.stdin.readline

n = int(input())

store = list(map(int, input().split()))

milk = 0

for i in range(n):
   if store[i] == milk % 3:
    milk += 1
print(milk)