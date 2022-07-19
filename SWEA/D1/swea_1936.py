# import sys

# sys.stdin = open("swea_1936_input.txt", "r")

a, b = map(str, input().split())

if a == '3' and b == '2' or a == '1' and b == '3' or a == '2' and b == '1':
    print("A")
elif b == '3' and a == '2' or b == '1' and a == '3' or b == '2' and a == '1':
    print("B")