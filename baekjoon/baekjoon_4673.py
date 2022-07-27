numbers = list(range(1, 10000))
list_ = []

for i in numbers:
    for j in str(i):
        i += int(j)

    if i < 10000:
        list_.append(i)

for i in set(list_):
    numbers.remove(i)

for i in numbers:
    print(i)