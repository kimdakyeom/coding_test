def solution(s):
    answer = len(s)
    for i in range(1, len(s) // 2 + 1):
        tmp, idx = "", 0
        while idx < len(s):
            n = 1
            word = s[idx:idx+i]
            while word == s[idx+i:idx+i+i]:
                idx, n = idx + i, n + 1
            if n != 1:
                tmp += (str(n) + word)
            else:
                tmp +=  word
            idx += i
        if len(tmp) < answer:
            answer = len(tmp)
    return answer