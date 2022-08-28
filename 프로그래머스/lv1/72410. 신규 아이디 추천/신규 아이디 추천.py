def solution(new_id):
    new_id = new_id.lower()

    answer = ""
    for i in new_id:
        if i.isalnum() or i in '-_.':
            answer += i

    while '..' in answer:
        answer = answer.replace('..', '.')
        
    answer = answer.strip('.')

    if answer == "":
        answer = "a"
    else:
        answer
    
    if len(answer) >= 16:
        answer = answer[:15]
        answer = answer.rstrip('.')
    elif len(answer) <= 3:
        answer = answer + answer[-1] * (3 - len(answer))
    
    return answer