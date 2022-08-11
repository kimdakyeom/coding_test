m, n = map(int, input().split())
x = 0
y = 0
direction = 0

com = []
d = []
ans = []

for i in range(n):
    com_, d_ = input().split()
    com.append(com_)
    d.append(int(d_))

for i in range(n):
    if com[i] == 'TURN':
        if d[i] == 0:
            if direction == 0:
                direction = 2
            elif direction == 1:
                direction = 3
            elif direction == 2:
                direction = 1
            elif direction == 3:
                direction = 0
        elif d[i] == 1:
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 0
            elif direction == 3:
                direction = 1
    elif com[i] == 'MOVE':
        if direction == 0:
            for j in range(int(d[i])):
                x += 1
        elif direction == 1:
            for j in range(int(d[i])):
                x -= 1
        elif direction == 2:
            for j in range(int(d[i])):
                y += 1
        elif direction == 3:
            for j in range(int(d[i])):
                y -= 1
    if(x < 0 or x > m or y < 0 or y > m):
        ans.append(-1)

if -1 in ans:
    print(-1)
else:
    print(x, y)