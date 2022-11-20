def solution(want, number, discount):
    answer = 0
    sale = {}
    for i in range(len(want)):
        sale[want[i]] = number[i]
    store_sale = {}
    for i in range(0, len(discount)-10+1):
        store_sale = {}
        for j in range(i, i+10):
            if discount[j] in store_sale:
                store_sale[discount[j]] += 1
            else:
                store_sale[discount[j]] = 1
        if store_sale == sale:
            answer += 1
    return answer