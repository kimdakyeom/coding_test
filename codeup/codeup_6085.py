w, h, b = input().split(" ")
w = int(w)
h = int(h)
b = int(b)

bit = w * h * b
mb = bit / 8 / 1024 / 1024

print("{:.2f} MB".format(mb))