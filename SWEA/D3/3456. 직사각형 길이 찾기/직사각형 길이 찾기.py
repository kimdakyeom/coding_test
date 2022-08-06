T = int(input())

for t in range(1, T+1):
    input_ = list(map(int, input().split()))
    list_ = [0] * 101

    for i in input_:
        list_[i] += 1
    for i in range(len(list_)):
        if list_[i] == 1:
            print(f'#{t} {i}')
        elif list_[i] == 3:
            print(f'#{t} {i}')