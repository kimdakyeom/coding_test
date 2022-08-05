import sys
input = sys.stdin.readline

n, m = map(int, input().split())
flag = True

for i in range(m):
    length = int(input())
    stacks = list(map(int, input().split()))
    for j in range(length-1):
        if stacks[j] < stacks[j+1]:
            flag = False
            break
    if not flag:
        break

print('Yes' if flag else 'No') 