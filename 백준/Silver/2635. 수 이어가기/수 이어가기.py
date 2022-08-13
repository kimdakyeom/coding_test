n = int(input())
max_length = 0

for j in range(n):
    ans_list= []
    ans_list.append(n)
    m = n - j
    ans_list.append(m)
    i = 2
    while True:
        ans_list.append(ans_list[i - 2] - ans_list[i - 1])
        if ans_list[i] < 0:
            ans_list.pop()
            break
        i += 1
    if max_length < len(ans_list):
        max_length = len(ans_list)
        ans = ans_list[:]
print(max_length)
final_ans = [str(ans[i]) for i in range(len(ans))]
print(' '.join(final_ans))