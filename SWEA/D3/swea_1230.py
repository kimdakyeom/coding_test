# import sys
# sys.stdin = open("swea_1230_input.txt", 'rt', encoding='UTF8')

for t in range(1, 11) :
    n = int(input())
    data = list(map(int, input().split()))
    o = int(input())
    order = list(input().split())

    for i in range(len(order)):
        if order[i] == 'I':
            idx = int(order[i+1])
            ran = int(order[i+2])
            list_ = []
            for j in range(i+3, i+3+ran):
                list_.append(order[j])
            for k in range(len(list_)):
                data.insert(idx+k, list_[k])
        elif order[i] == 'D':
            idx = int(order[i+1])
            ran = int(order[i+2])
            for j in range(ran):
                data.pop(idx)
        elif order[i] == 'A':
            ran = int(order[i+1])
            list_ = []
            for j in range(i+2, i+2+ran):
                list_.append(order[j])
            for k in range(len(list_)):
                data.append(list_[k])

    print(f'#{t}', end=' ')
    print(*data[:10])