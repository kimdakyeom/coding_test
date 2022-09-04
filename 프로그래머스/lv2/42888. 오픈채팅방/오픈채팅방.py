def solution(record):
    answer = []
    dic = {}

    for i in record:
        data = i.split(' ')
        if len(data) == 3:
            dic[data[1]] = data[2]
    
    for i in record:
        data = i.split(' ')
        if data[0] == "Enter":
            answer.append(f'{dic[data[1]]}님이 들어왔습니다.')
        elif data[0] == "Leave":
            answer.append(f'{dic[data[1]]}님이 나갔습니다.')
    return answer