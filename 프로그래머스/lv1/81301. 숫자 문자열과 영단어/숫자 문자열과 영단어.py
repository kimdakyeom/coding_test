def solution(s):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for i in range(len(s)):
        for j in range(len(num_list)):
            if s[i:i+3] == num_list[j]:
                s = s.replace(s[i:i+3], str(j))
            if s[i:i+4] == num_list[j]:
                s = s.replace(s[i:i+4], str(j))
            if s[i:i+5] == num_list[j]:
                s = s.replace(s[i:i+5], str(j))

    return int(s)