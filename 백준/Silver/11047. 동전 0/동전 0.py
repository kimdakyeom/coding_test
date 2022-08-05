n, money = map(int, input().split())

dict = {}

for tc in range(n):
    charge = int(input())
    dict[charge] = 0

sum = 0
for i in reversed(dict):
    dict[i] += money // i
    money = money % i
    sum += dict.get(i)
print(sum)