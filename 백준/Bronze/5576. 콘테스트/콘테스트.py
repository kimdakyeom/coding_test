w = []
k = []

for i in range(10):
    w.append(int(input()))
for i in range(10, 20):
    k.append(int(input()))
w.sort(reverse=True)
k.sort(reverse=True)

w_sum = w[0] + w[1] + w[2]
k_sum = k[0] + k[1] + k[2]

print(w_sum, k_sum, end=' ')