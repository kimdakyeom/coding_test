fruit = int(input())

list_ = []
max_w = 0
max_h = 0
max_w_idx = 0
max_h_idx = 0

for i in range(6):
    tmp = list(map(int, input().split()))
    list_.append(tmp)

    if tmp[0] == 1 or tmp[0] == 2:
        if max_w < tmp[1]:
            max_w = tmp[1]
            max_w_idx = i
    else:
        if max_h < tmp[1]:
            max_h = tmp[1]
            max_h_idx = i

index_list = [list_[max_h_idx - 1], list_[(max_h_idx + 1) % 6], list_[max_w_idx - 1], list_[(max_w_idx + 1) % 6]]

mul = 1
for i in list_:
    if i not in index_list:
        mul *= i[1]
ans = (max_w * max_h - mul) * fruit
print(ans)