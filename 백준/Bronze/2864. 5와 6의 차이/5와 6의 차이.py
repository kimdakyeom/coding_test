a, b = input().split()

min_a = a.replace("6", "5")
min_b = b.replace("6", "5")
min = int(min_a) + int(min_b)

max_a = a.replace("5", "6")
max_b = b.replace("5", "6")
max = int(max_a) + int(max_b)

print(min, max)