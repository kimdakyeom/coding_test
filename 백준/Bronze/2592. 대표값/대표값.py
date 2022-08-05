num = []

for tc in range(10):
    num.append(int(input()))

sum_ = 0
dict_ = {}

for i in num:
    sum_ += i
    if i not in dict_:
        dict_[i] = 0
    elif i in dict_:
        dict_[i] += 1
avg = sum_ // 10
print(avg)
print(max(dict_, key=dict_.get))