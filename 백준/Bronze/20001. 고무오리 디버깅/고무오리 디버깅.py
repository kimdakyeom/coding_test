import sys
input = sys.stdin.readline

start = input()
sum = 0

while True:
    word = input().split('\n')[0]
    if word == "고무오리 디버깅 끝":
        if sum == 0:
            print("고무오리야 사랑해")
            break
        else:
            print("힝구")
            break
    elif word == "문제":
        sum -= 1
    elif word == "고무오리":
        if sum == 0:
            sum -= 2
        else:
            sum += 1