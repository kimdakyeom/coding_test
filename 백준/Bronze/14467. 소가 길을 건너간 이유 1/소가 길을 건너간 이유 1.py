n = int(input())
dic = {}

sum_ = 0
for i in range(n):
    num, pos = map(int, input().split())
    if num not in dic:
        dic[num] = pos
    elif num in dic:
        if pos != dic.get(num):
            sum_ += 1
            dic[num] = pos

print(sum_)