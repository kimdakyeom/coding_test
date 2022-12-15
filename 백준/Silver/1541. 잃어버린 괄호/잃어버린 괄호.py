exp = input()
exp_list = exp.split('-')

answer_list = []
for i in exp_list:
    tmp = 0
    if '+' in i:
        i_list = i.split('+')
        for j in i_list:
            tmp += int(j)
        answer_list.append(tmp)
    else:
        answer_list.append(int(i))
answer = answer_list[0]
for i in range(1, len(answer_list)):
    answer -= answer_list[i]
print(answer)