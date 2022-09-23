from collections import deque

def solution(rotate):
    def check(s):
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if not stack:
                    return False
                x = stack.pop()
                if i == ')' and x != '(':
                    return False
                elif i == ']' and x != '[':
                    return False
                elif i == '}' and x != '{':
                    return False
        return len(stack) == 0
        
    rotate = deque(rotate)
    answer = 0
    
    for i in range(len(rotate)):
        rotate.rotate(-1)
        if check(rotate):
            answer += 1
    return answer
