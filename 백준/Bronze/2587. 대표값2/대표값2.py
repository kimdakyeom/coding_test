num_list = []

for i in range(5):
    num_list.append(int(input()))
num_list.sort()

sum = 0
for i in num_list:
    sum += i
print(int(sum/5))
print(num_list[2])