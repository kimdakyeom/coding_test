# import sys

# sys.stdin = open("swea_2056_input.txt", "r")

cal = [31,28,31,30,31,30,31,31,30,31,30,31]
n = int(input())

for i in range(1, n+1):
    num = input()
    if int(num[4:6]) > 0 and int(num[4:6]) < 13:
        if(int(num[6:8]) <= cal[int(num[4:6])-1]):
            print(f'#{i} {num[0:4]}/{num[4:6]}/{num[6:8]}')
        else:
            print(f'#{i} -1')
    else:
            print(f'#{i} -1')