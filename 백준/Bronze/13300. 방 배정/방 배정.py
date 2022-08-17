import math
n, k = map(int, input().split())
female = [0] * 7
male = [0] * 7

for t in range(n):
    gender, grade = map(int, input().split())

    if gender == 0:
        female[grade] += 1
    elif gender == 1:
        male[grade] += 1

room = 0

for i in range(1, 7):
    room += math.ceil(female[i] / k)
    room += math.ceil(male[i] / k)
print(room)