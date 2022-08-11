a, b, c = map(int, input().split())

start1, end1 = map(int, input().split())
start2, end2 = map(int, input().split())
start3, end3 = map(int, input().split())

max_ = max(start1, end1, start2, end2, start3, end3)
list1 = [0] * max_
list2 = [0] * max_
list3 = [0] * max_

for i in range(start1, end1):
    list1[i] = 1
for i in range(start2, end2):
    list2[i] = 1
for i in range(start3, end3):
    list3[i] = 1

sum_ = 0
for i in range(1, max_):
    list_ = []
    list_.append(list1[i])
    list_.append(list2[i])
    list_.append(list3[i])
    if list_.count(1) == 1:
        sum_ += 1 * a
    elif list_.count(1) == 2:
        sum_ += 2 * b
    elif list_.count(1) == 3:
        sum_ += 3 * c
print(sum_)