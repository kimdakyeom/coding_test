word = input()
WORD = word.upper()

list = [0] * 27
answer = []

for i in WORD:
    asci = ord(i) - 64

    list[asci] += 1

# print(max(list))
for i in range(len(list)):
    if list[i] == max(list):
        answer.append(chr(i+64))

if len(answer) >= 2:
    print("?")
else:
    print(*answer)