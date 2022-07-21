import sys
sys.stdin = open("swea_1974_input.txt", "r")

t = int(input())

for T in range(1, t+1):
    num = [list(map(int, input().split())) for i in range(9)]
    rec = []
    
    for i in range(3):
        for j in range(3):
            rec.append(num[i][j])
    print(rec)