def solution(order):
    con = []
    i = 1
    now = 0
    while True:
        con.append(i)
        while order[now] == con[-1]:
            con.pop()
            now += 1
            if len(con) == 0:
                break
        i += 1
        if i == len(order) + 1:
            break
    return now