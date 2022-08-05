import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    vps = input()
    stack = []
    stack.append(0)
    for j in vps:
        stack.append(j)
        if stack[-2] == '(' and stack[-1] == ')':
            stack.pop()
            stack.pop()

    if len(stack) == 2:
        print("YES")
    else:
        print("NO")