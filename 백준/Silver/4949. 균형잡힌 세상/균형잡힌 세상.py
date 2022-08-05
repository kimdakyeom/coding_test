while True:
    sen = input()

    if sen == ".":
        break

    stack = []
    stack.append(0)

    for i in sen:
        if i == "(" or i == ")" or i == "[" or i == "]":
            stack.append(i)
            if stack[-1] == ")" and stack[-2] == "(":
                stack.pop()
                stack.pop()
            elif stack[-1] == "]" and stack[-2] == "[":
                stack.pop()
                stack.pop()

    if len(stack) == 1:
        print("yes")
    else:
        print("no")