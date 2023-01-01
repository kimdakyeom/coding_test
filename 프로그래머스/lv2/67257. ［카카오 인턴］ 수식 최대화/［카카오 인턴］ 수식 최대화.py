from itertools import permutations
def operation(num1, num2, op):
    if op == '+':
        return str(int(num1) + int(num2))
    elif op == '-':
        return str(int(num1) - int(num2))
    elif op == '*':
        return str(int(num1) * int(num2))
    
def calculate(ex, op):
    split_ex = []
    tmp = ''
    for i in ex:
        if i == '*' or i == '+' or i == '-':
            split_ex.append(int(tmp))
            tmp = ''
            split_ex.append(i)
        else:
            tmp += i
    split_ex.append(int(tmp))
    
    for o in op:
        stack = []
        while len(split_ex) != 0:
            tmp = split_ex.pop(0)
            if tmp == o:
                stack.append(operation(stack.pop(), split_ex.pop(0), o))
            else:
                stack.append(tmp)
        split_ex = stack
    return abs(int(split_ex[0]))
    
def solution(expression):
    answer = []
    cal = ['*', '+', '-']
    op = []
    for i in permutations(cal, 3):
        op.append(i)
    for i in op:
        answer.append(calculate(expression, i))
    return max(answer)