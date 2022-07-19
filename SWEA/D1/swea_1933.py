# import sys

# sys.stdin = open("swea_1933_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i, end=' ')