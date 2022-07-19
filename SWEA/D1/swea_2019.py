# import sys

# sys.stdin = open("swea_2019_input.txt", "r")

n = int(input())
result = 1
print(result, end=' ')

for i in range(1, n+1):
    result *= 2
    print(result, end=' ')