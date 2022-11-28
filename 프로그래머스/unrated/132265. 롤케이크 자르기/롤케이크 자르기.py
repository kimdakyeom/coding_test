from collections import Counter
def solution(topping):
    answer = 0
    toppings = Counter(topping)
    new_toppings = set()
    for i in topping:
        toppings[i] -= 1
        new_toppings.add(i)
        if toppings[i] == 0:
            toppings.pop(i)
        if len(new_toppings) == len(toppings):
            answer += 1
    return answer