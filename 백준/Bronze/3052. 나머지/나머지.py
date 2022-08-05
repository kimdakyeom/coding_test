a = []
b = []

for i in range(10):
    a.append(int(input()))

for i in range(len(a)):
    b.append(a[i] % 42)

print(len(list(set(b))))