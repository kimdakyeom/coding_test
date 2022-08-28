def solution(price, money, count):
    all_price = 0
    for i in range(1, count + 1):
        price_i = price * i
        all_price += price_i

    answer = all_price - money

    if answer > 0:
        return answer
    else:
        return 0