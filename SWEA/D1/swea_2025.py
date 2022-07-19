# import sys

# sys.stdin = open("swea_2025_input.txt", "r")

n = int(input())
sum = 0

for i in range(1, n+1):
    sum += i
print(sum)