from functools import reduce

def solution(clothes):
    answer = 0
    dic_ = {}
    list_ = []

    for i in clothes:
        if i[1] not in dic_:
            dic_[i[1]] = 1
        else:
            dic_[i[1]] += 1

    for i in dic_.values():
        list_.append(i + 1)
        
    answer = reduce(lambda x, y: x * y, list_)
    return answer - 1