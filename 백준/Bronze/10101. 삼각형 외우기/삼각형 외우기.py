tri = []

for i in range(3):
    tri.append(int(input()))

sum_ = tri[0] + tri[1] + tri[2]

if sum_ == 180:
    if tri[0] == tri[1] == tri[2]:
        print('Equilateral')
    elif tri[0] == tri[1] or tri[0] == tri[2] or tri[1] == tri[2]:
        print('Isosceles')
    else:
        print('Scalene')
elif sum_ != 180:
    print('Error')