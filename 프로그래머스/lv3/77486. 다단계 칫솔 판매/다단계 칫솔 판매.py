def solution(enroll, referral, seller, amount):
    answer = []
    money = dict()
    subject = dict()

    for i in range(len(enroll)):
        subject[enroll[i]] = referral[i]
        money[enroll[i]] = 0

    for idx, i in enumerate(seller):
        name = i
        value = amount[idx] * 100
        while True:
            if value * 0.1 < 1:
                money[name] += value
                break
            money[name] += value - int(value * 0.1)
            if subject[name] == "-":
                break
            name = subject[name]
            value = int(value * 0.1)
    return [i for i in money.values()]