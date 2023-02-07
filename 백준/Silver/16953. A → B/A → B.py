import sys
from pprint import pprint
input = sys.stdin.readline

a, b = map(str, input().split())
cnt = 0

while True:
    if b[-1] == '1':
        b = b[:-1]
        cnt += 1
    elif not int(b[-1]) % 2: #짝수
        b = str(int(b) // 2)
        cnt += 1
    elif int(b[-1]) % 2: # 홀수
        if a != b:
            cnt = -1
            break
    if int(a) > int(b):
        cnt = -1
        break
    if int(a) == int(b):
        cnt += 1
        break
print(cnt)