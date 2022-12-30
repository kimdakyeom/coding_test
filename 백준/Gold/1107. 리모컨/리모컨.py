import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

if m != 0:
    b = list(map(int, input().split()))
else:
    b = []

answer = abs(100-n)
for i in range(1000001):
    nums = list(str(i))
    flag = False

    for k in nums:
        if int(k) in b:
            flag = True
            break
    if flag:
        continue
    else:
        answer = min(answer, abs(n-i)+len(str(i)))
print(answer)