import sys
# sys.stdin = open("input2.txt", "r")

# input = sys.stdin.readline
n = int(input())
star = ["***", "* *", "***"]
cnt = 0

def pattern(star):
    arr = []
    for i in range(len(star)*3):
        if i // len(star) == 1:
            arr.append(star[i%len(star)] + " " * len(star) + star[i%len(star)])
        else:
            arr.append(star[i%len(star)] * 3)
    # print(arr)
    return arr

while n > 3:
    n /= 3
    cnt += 1

for i in range(cnt):
    star = pattern(star)

for i in star:
    print(i)