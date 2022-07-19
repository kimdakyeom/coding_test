# import sys

# sys.stdin = open("swea_2063_input.txt", "r")

n = int(input())
num = list(map(int, input().split()))
mid = round(n / 2)

sort_num = sorted(num)
print(sort_num[mid-1])