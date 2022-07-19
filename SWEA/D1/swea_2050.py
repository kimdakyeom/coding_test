# import sys

# sys.stdin = open("swea_2050_input.txt", "r")

alpha = input()

for i in alpha:
    asc = ord(i)
    print(asc-64, end=' ')