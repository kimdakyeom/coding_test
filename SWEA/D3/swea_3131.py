n = 10 ** 6 + 1
list_ = [1] * n
list_[0], list_[1] = 0, 0

for i in range(2, n):
    if list_[i] == 1:
        for j in range(i * 2, n, i):
            list_[j] = 0
for i in range(n):
    if list_[i] == 1:
        print(i, end=' ')