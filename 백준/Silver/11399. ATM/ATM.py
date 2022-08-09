n = int(input())

num = list(map(int, input().split()))
num.sort()
sum_ = 0
for i in range(n):
    for j in range(i+1):
        sum_ += num[j]
print(sum_)