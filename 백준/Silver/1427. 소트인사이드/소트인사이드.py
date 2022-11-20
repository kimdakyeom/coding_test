n = int(input())
list_ = []

for i in str(n):
    list_.append(int(i))
list_.sort(reverse=True)

for i in list_:
    print(i, end="")