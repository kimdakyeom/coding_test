def solution(s):
    answer = ''
    word_list = list(s)
    k = 0

    for i in range(len(s)):
        if word_list[i].isalpha and k % 2 == 0 and word_list[i].islower():
            answer += word_list[i].upper()
            k += 1
        elif word_list[i].isalpha and k % 2 == 0 and word_list[i].isupper():
            answer += word_list[i]
            k += 1
        elif word_list[i] == ' ':
            k = 0
            answer += ' '
        elif k % 2 == 1 and word_list[i].isupper():
            answer += word_list[i].lower()
            k += 1
        elif k % 2 == 1 and word_list[i].islower():
            k += 1
            answer += word_list[i]
    return answer