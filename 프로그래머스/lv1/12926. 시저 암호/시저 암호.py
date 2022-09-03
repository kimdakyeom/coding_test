def solution(s, n):
    answer = ''
    s = list(s)
    for i in s:
        if 65 <= ord(i) <= 90:
            if ord(i) - 64 + n >= 27:
                answer += chr((ord(i) - 64 + n) % 26 + 64)
            else:
                answer += chr(ord(i) - 64 + n + 64)
        elif 97 <= ord(i) <= 122:
            if ord(i) - 96 + n >= 27:
                answer += chr((ord(i) - 96 + n) % 26 + 96)
            else:
                answer += chr(ord(i) - 96 + n + 96)
        elif i == " ":
            answer += " "
    return answer