cnt = 0
name_list = []
for i in range(5):
    name = input()
    name_list.append(name)

for i in range(len(name_list)):
    if 'FBI' in name_list[i]:
        cnt += 1
        print(i+1, end=' ')
if cnt == 0:
    print('HE GOT AWAY!')