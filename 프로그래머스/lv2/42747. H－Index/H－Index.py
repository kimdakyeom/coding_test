def solution(citations):
    citations.sort(reverse = True)
    answer = 0

    for i in range(len(citations)):
        if i + 1 <= citations[i]:
            answer = i + 1
        if i + 1 > citations[i]:
            break
    return answer