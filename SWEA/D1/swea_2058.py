# import sys

# sys.stdin = open("swea_2058_input.txt", "r")

n = int(input())
str_n = str(n)
sum = 0

for i in str_n:
    sum += int(i)
print(sum)