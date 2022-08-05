suyeol = []

for i in range(1, 1001):
    suyeol.extend([i] * i)

a, b = map(int, input().split())
sum = 0

for i in range(a-1, b):
    sum += suyeol[i]
    
print(sum)