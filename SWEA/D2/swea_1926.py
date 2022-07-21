# import sys
# sys.stdin = open("swea_1926_input.txt", "r")

n = int(input())
result = []

for i in range(1, n+1):
    new_i = str(i)
    cnt = 0

    for k in new_i:
        if k == "3" or k == "6" or k == "9":
            cnt += 1
        if cnt == 1:
            new_i = "-"
        elif cnt == 2:
            new_i = "--"
        elif cnt == 3:
            new_i == "---"
        else:
            new_i = new_i
    print(new_i, end=' ')