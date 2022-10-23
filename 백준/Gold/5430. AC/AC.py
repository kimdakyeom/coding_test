from collections import deque

for tc in range(int(input())):
    P = input()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(","))
    if n == 0:
        arr = []

    rev = 0
    for p in P:
        if p == "R":
            rev += 1
        elif p == "D":
            if len(arr) < 1:
                print("error")
                flag = 1
                break
            else:
                if rev % 2 == 0:
                    arr.popleft()
                else:
                    arr.pop()
    else:
        if rev % 2 == 0:
            print("[" + ",".join(arr) + "]")
        else:
            arr.reverse()
            print("[" + ",".join(arr) + "]")