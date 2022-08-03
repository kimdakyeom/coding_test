min_ = int(input())
max_ = int(input())
list_ = []

for i in range(min_, max_+1):
    error = 0
    if i > 0:
        for j in range(2, i):
            if i % j == 0:
                error += 1
                break
        if error == 0:
            list_.append(i)

if 1 in list_:
    list_.remove(1)
    
if len(list_) > 0:
    print(sum(list_))
    print(min(list_))
else:
    print(-1)