numbers = list(range(1, 10000))
list = []
for i in numbers:
    for j in str(i) :
        i += int(j)
    if i < 10000:
        list.append(i)
for i in set(list): # 중복된 숫자 정리
    numbers.remove(i)
for i in numbers:
    print(i)