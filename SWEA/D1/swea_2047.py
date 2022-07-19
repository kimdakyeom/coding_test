# import sys

# sys.stdin = open("swea_2047_input.txt", "r")

sen = input()

for i in sen:
    little = ord(i)
    if little >= 97 and little <= 122:
        little -= 32
        little = chr(little)
    else:
        little = i
    print(little, end='')