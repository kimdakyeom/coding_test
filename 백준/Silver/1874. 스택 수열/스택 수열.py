n = int(input())
stack = []
answer = []
cur = 1
flag = False

for _ in range(n):
    num = int(input())
    while cur <= num:
        stack.append(cur)
        answer.append("+")
        cur += 1
    if stack[-1] == num:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = True
        break
if flag == False:
    for i in answer:
        print(i)