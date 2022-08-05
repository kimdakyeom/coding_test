cro = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

alpha = input()
result = 0

for i in cro:
    alpha = alpha.replace(i, "*")

for i in alpha:
    result += 1
print(result)