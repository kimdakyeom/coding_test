n = int(input())

box = [list(map(int, input().split())) for _ in range(n)]
new_box = []

for top in range(1, 7):
    for i in range(n):
        tmp = []
        if box[i].index(top) == 0:
            for j in range(1, 7):
                if j == top or j == box[i][5]:
                    continue
                else:
                    tmp.append(j)
            top = box[i][5]
        elif box[i].index(top) == 1:
            for j in range(1, 7):
                if j == top or j == box[i][3]:
                    continue
                else:
                    tmp.append(j)
            top = box[i][3]
        elif box[i].index(top) == 2:
            for j in range(1, 7):
                if j == top or j == box[i][4]:
                    continue
                else:
                    tmp.append(j)
            top = box[i][4]
        elif box[i].index(top) == 3:
            for j in range(1, 7):
                if j == top or j == box[i][1]:
                    continue
                else:
                    tmp.append(j)
            top = box[i][1]
        elif box[i].index(top) == 4:
            for j in range(1, 7):
                if j == top or j == box[i][2]:
                    continue
                else:
                    tmp.append(j)
            top = box[i][2]
        elif box[i].index(top) == 5:
            for j in range(1, 7):
                if j == top or j == box[i][0]:
                    continue
                else:
                    tmp.append(j)
            top = box[i][0]
        new_box.append(tmp)

max_list = []
for i in range(len(new_box)):
    max_list.append(max(new_box[i]))

sum_list = []
for i in range(0, len(max_list), n):
    sum_ = 0
    for j in range(i, i+n):
        sum_ += max_list[j]
    sum_list.append(sum_)
print(max(sum_list))