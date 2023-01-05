import sys
input = sys.stdin.readlines

colors = []
nums = []
flag = True
inp = input()
for i in range(5):
    c, n = inp[i].rstrip('\n').split()[0], int(inp[i].rstrip('\n').split()[1])
    colors.append(c)
    nums.append(n)
nums.sort()

for i in range(1, len(nums)):
    if nums[i] - nums[i-1] != 1:
        flag = False
        break

answer = 0
c_dict = {}
for i in colors:
    if i not in c_dict:
        c_dict[i] = 1
    else:
        c_dict[i] += 1

n_dict = {}
for i in nums:
    if i not in n_dict:
        n_dict[i] = 1
    else:
        n_dict[i] += 1

sorted_n = sorted(n_dict.items(), key=lambda x: (x[1], -x[0]), reverse=True)
if len(c_dict) == 1 and flag == True:
    answer = 900 + nums[-1]
elif len(sorted_n) == 2 and sorted_n[0][1] == 4:
    answer = 800 + sorted_n[0][0]
elif len(sorted_n) == 2 and sorted_n[0][1] == 3:
    answer = 700 + sorted_n[0][0] * 10 + sorted_n[1][0]
elif len(c_dict) == 1:
    answer = 600 + sorted_n[-1][0]
elif flag == True:
    answer = 500 + sorted_n[-1][0]
elif len(sorted_n) == 3 and sorted_n[0][1] == 3:
    answer = 400 + sorted_n[0][0]
elif len(sorted_n) == 3 and sorted_n[0][1] == 2:
    answer = 300 + sorted_n[1][0] * 10 + sorted_n[0][0]
elif len(sorted_n) == 4:
    answer = 200 + sorted_n[0][0]
else:
    answer = 100 + sorted_n[-1][0]
print(answer)