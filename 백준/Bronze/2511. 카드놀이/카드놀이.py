a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_sum = 0
b_sum = 0

history = "D"

for i in range(len(a)):
    if a[i] > b[i]:
        a_sum += 3
        history = "A"
    elif a[i] < b[i]:
        b_sum += 3
        history = "B"
    elif a[i] == b[i]:
        a_sum += 1
        b_sum += 1

print(a_sum, b_sum)
if a_sum > b_sum:
    print("A")
elif a_sum < b_sum:
    print("B")
elif a_sum == b_sum:
    if history == "A":
        print("A")
    if history == "B":
        print("B")
    if history == "D":
        print("D")