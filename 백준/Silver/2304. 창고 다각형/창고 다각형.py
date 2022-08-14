T = int(input())
pillar = []

max_x = 1
max_y = 0

for t in range(T):
    x, y = map(int, input().split())
    pillar.append((x, y))

    if max_x < x:
        max_x = x
    if max_y < y:
        max_y = y
        max_idx = x

pillar_list = [0] * (max_x + 1)

for X, Y in pillar:
    pillar_list[X] = Y

ans = 0
tmp = 0

for i in range(max_idx + 1):
    if pillar_list[i] > tmp:
        tmp = pillar_list[i]
    ans += tmp
tmp = 0
for i in range(max_x, max_idx, -1):
    if pillar_list[i] > tmp:
        tmp = pillar_list[i]
    ans += tmp
print(ans)