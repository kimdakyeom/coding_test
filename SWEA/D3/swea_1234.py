# import sys
# sys.stdin = open("swea_1234_input.txt", 'rt', encoding='UTF8')

for t in range(1, 11):
    n, pw = input().split()
    pw = str(pw)
    stack = []

    for i in pw:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    result = ''.join(stack)
    print(f'#{t} {result}')