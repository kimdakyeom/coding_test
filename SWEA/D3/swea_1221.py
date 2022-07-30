# import sys
# sys.stdin = open("swea_1221_input.txt", 'rt', encoding='UTF8')

number = {
    'ZRO' : 0,
    'ONE' : 1,
    'TWO' : 2,
    'THR' : 3,
    'FOR' : 4,
    'FIV' : 5,
    'SIX' : 6,
    'SVN' : 7,
    'EGT' : 8,
    'NIN' : 9
}

T = int(input())

for t in range(1, T+1):
    tc, length = input().split()
    length = int(length)

    string = list(input().split())
    
    list_ = []

    for i in string:
        list_.append(number[i])
    list_.sort()

    new_list = {v:k for k, v in number.items()}

    print(f'#{t}')
    for i in list_:
        print(new_list.get(i), end=' ')
    print()