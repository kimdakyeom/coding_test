def solution(array, commands):
    answer = []
    for command in range(len(commands)):
        i = commands[command][0] - 1
        j = commands[command][1] - 1
        k = commands[command][2]

        new_array = array[i:j+1]
        new_array.sort()
        answer.append(new_array[k-1])
    return answer