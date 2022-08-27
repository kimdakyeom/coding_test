def solution(survey, choices):
    dic_ = {'R' : 0,
    'T' : 0,
    'C' : 0,
    'F' : 0,
    'J' : 0,
    'M' : 0,
    'A' : 0,
    'N' : 0
    }
    for i in range(len(survey)):
        if choices[i] == 1:
            dic_[survey[i][0]] += 3
        if choices[i] == 2:
            dic_[survey[i][0]] += 2
        if choices[i] == 3:
            dic_[survey[i][0]] += 1
        if choices[i] == 4:
            continue
        if choices[i] == 5:
            dic_[survey[i][1]] += 1
        if choices[i] == 6:
            dic_[survey[i][1]] += 2
        if choices[i] == 7:
            dic_[survey[i][1]] += 3
    
    answer = '' 
    
    if dic_['R'] >= dic_['T']:
        answer += 'R'
    else:
        answer += 'T'
    if dic_['C'] >= dic_['F']:
        answer += 'C'
    else:
        answer += 'F'
    if dic_['J'] >= dic_['M']:
        answer += 'J'
    else:
        answer += 'M'
    if dic_['A'] >= dic_['N']:
        answer += 'A'
    else:
        answer += 'N'

    return answer