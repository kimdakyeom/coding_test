# import sys
# sys.stdin = open("swea_11688_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    dir = input()
    left = 1
    right = 1
    
    for i in dir:
        if i == "L":
            left = left
            right = left + right
        elif i == "R":
            left = left + right
            right = right
    
    print(f'#{t} {left} {right}')