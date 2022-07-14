n = int(input())
m = int(input())

print(n * (m // 1 % 10))
print(n * (m // 10 % 10))
print(n * (m // 100 % 10))
print(n * m)