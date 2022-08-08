T = int(input())

for t in range(1, T+1):
    price = int(input())
    count = int(input())

    for i in range(count):
        
        q, p = map(int, input().split())
        price += q * p

    print(price)