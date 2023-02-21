import sys
input = sys.stdin.readline

n = int(input())
play = []

for i in range(n):
    play.append(list(map(int, input().rstrip())))

result = []

def check_play(x, y, n):
    global result
    tmp = []
    for i in range(x, x+n):
        for j in range(y, y+n):
            tmp.append(play[i][j])
    if tmp == [0 for i in range(n*n)]:
        result.append(0)
    elif tmp == [1 for i in range(n*n)]:
        result.append(1)
    else:
        result.append("(")
        check_play(x, y, n//2)
        check_play(x, y + n//2, n//2)
        check_play(x + n//2, y, n//2)
        check_play(x + n//2, y + n//2, n//2)
        result.append(")")
    return result

result = check_play(0, 0, n)
print(*result, sep='')