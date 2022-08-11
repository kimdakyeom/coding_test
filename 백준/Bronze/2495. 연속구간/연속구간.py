for i in range(3):
    s = list(input())
    
    sum_ = 0
    sum_list = []
    for j in range(len(s) - 1):
        if s[j] == s[j+1]:
            sum_ += 1
        else:
            sum_ = 0
        sum_list.append(sum_)
    print(max(sum_list) + 1)