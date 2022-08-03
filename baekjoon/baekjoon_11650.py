n = int(input())
list_ = []

for tc in range(n):
    x, y = map(int, input().split())
    list_.append([x, y])
list_ = sorted(list_)

for i in range(n):
    print(list_[i][0], list_[i][1])