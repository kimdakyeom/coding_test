def solution(elements):
    new_elements = elements * 2
    sum_list = []
    for k in range(1, len(elements)+1):
        for i in range(len(elements)):
            sum_list.append(sum(new_elements[i:i+k]))
    return len(set(sum_list))