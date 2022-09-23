def solution(n):
    answer = 0
    origin_one = bin(n)[2:].count("1")
    new_one = 0

    while new_one != origin_one:
        n += 1
        new_one = bin(n)[2:].count("1")
    answer = n

    return answer