n, m = map(int, input().split())
T = int(input())

width = [0, m]
height = [0, n]

for t in range(T):
    wh, num = map(int, input().split())
    if wh == 0:
        width.append(num)
    elif wh == 1:
        height.append(num)
width.sort()
height.sort()
area = []

for i in range(1, len(width)):
    for j in range(1, len(height)):
        ans_w = width[i] - width[i-1]
        ans_h = height[j] - height[j-1]
        area.append(ans_w * ans_h)
print(max(area))