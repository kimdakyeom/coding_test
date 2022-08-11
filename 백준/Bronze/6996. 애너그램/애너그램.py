n = int(input())

for i in range(n):
    a, b = map(str, input().split())

    a_ = sorted(list(a))
    b_ = sorted(list(b))

    if a_ == b_:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')