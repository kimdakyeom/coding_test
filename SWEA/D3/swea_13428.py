import sys
sys.stdin = open("swea_13428_input.txt", "r")

T = int(input())

for t in range(1, T+1):
    num = list(input())
    max = int(''.join(num))
    min = int(''.join(num))

    for i in range(len(num)-1):
        for j in range(i+1, len(num)):
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp
            result = ' '.join(s for s in num)
            result = result.replace(" ", "")

    if int(result) > max:
        max = int(result)
    elif int(result) < min:
        min = int(result)
    
    print(f'#{t} {min} {max}')