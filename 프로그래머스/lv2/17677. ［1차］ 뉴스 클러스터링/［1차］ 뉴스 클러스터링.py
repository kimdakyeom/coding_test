import math

def solution(str1, str2):
    answer = 0
    s1 = two(str1)
    s2 = two(str2)

    if s1 == [] and s2 == []:
        return 65536
    
    s1_copy = s1.copy()
    s2_copy = s2.copy()

    inter = []
    for i in s1:
        if i in s2_copy:
            inter.append(i)
            s1_copy.remove(i)
            s2_copy.remove(i)
    
    union = inter + s1_copy + s2_copy
    answer = math.floor((len(inter) / len(union)) * 65536)
    return answer

def two(s):
    s = s.upper()
    a = []
    for i in range(len(s) - 1):
        if s[i:i + 2].isalpha():
            a.append(s[i:i + 2])
    return a