# import sys
# sys.stdin = open("swea_2007_input.txt", "r")

t = int(input())

for T in range(1, t+1):
    sen = input()

    for i in range(1, len(sen)):
        if sen[0:i] == sen[i:i+i]:
            print(f'#{T} {i}')
            break