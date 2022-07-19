# import sys

# sys.stdin = open("swea_2029_input.txt", "r")

n = int(input())

for i in range(1, n+1):
    a, b = map(int, input().split(" "))
    print(f'#{i} {a//b} {a%b}')