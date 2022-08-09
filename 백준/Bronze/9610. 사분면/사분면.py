T = int(input())

q = [0, 0, 0, 0, 0]

for t in range(T):
    x, y = map(int, input().split())

    if x == 0 or y == 0:
        q[4] += 1
    elif x > 0 and y > 0:
        q[0] += 1
    elif x < 0 and y > 0:
        q[1] += 1
    elif x < 0 and y < 0:
        q[2] += 1
    elif x > 0 and y < 0:
        q[3] += 1

print(f'Q1: {q[0]}')
print(f'Q2: {q[1]}')
print(f'Q3: {q[2]}')
print(f'Q4: {q[3]}')
print(f'AXIS: {q[4]}')