tebo = input()

tebo_sp = tebo.split("(^0^)")

for i in range(len(tebo_sp)):
    print(tebo_sp[i].count("@"), end=' ')