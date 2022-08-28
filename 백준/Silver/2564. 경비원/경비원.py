def get_distance(x, y):
    if x == 1:
        return y
    elif x == 2:
        return w + h + w - y
    elif x == 3:
        return w + h + w + h - y
    elif x == 4:
        return w + y

w, h = map(int, input().split())

stores = []
for t in range(int(input()) + 1):
    x, y = map(int, input().split())
    stores.append(get_distance(x, y))

sum_ = 0

for i in range(len(stores)):
    dis_in = abs(stores[-1] - stores[i])
    dis_out = 2 * (w + h) - dis_in
    sum_ += min(dis_in, dis_out)
print(sum_)