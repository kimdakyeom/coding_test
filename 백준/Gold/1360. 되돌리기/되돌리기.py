import sys
# sys.stdin = open("input2.txt", "r")

input = sys.stdin.readline
n = int(input())

text = ''
undo = []
for _ in range(n):
    tu, char, time = input().split()
    if tu == "type":
        time = int(time)
        text += char
        undo.append((time, text))
    else:
        char, time = int(char), int(time)
        for i in range(len(undo)-1, -1, -1):
            if undo[i][0] < time-char:
                text = undo[i][1]
                undo.append((time, text))
                break
        else:
            text = ''
            undo.append((time, text))
# print(undo)
print(undo[-1][1])