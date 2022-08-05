h, m = map(int, input().split(" "))
oven = int(input())

while oven >= 60:
    oven -= 60
    h += 1

if m + oven >= 60:
    if h + 1 >= 24:
        print(h + 1 - 24, m + oven - 60)
    else:
        print(h + 1, m + oven - 60)
elif m + oven < 60:
    if h >= 24:
        print(h-24, m + oven)
    else:    
        print(h, m + oven)