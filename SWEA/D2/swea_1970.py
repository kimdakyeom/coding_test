# import sys
# sys.stdin = open("swea_1970_input.txt", "r")

t = int(input())

for i in range(1, t+1):
    m = int(input())
    m_50000, m_10000, m_5000, m_1000, m_500, m_100, m_50, m_10 = 0, 0, 0, 0, 0, 0, 0, 0

    while m >= 10:
        if m >= 50000:
            m_50000 = m // 50000
            m = m % 50000
        elif m >= 10000:
            m_10000 = m // 10000
            m = m % 10000
        elif m >= 5000:
            m_5000 = m // 5000
            m = m % 5000
        elif m >= 1000:
            m_1000 = m // 1000
            m = m % 1000
        elif m >= 500:
            m_500 = m // 500
            m = m % 500
        elif m >= 100:
            m_100 = m // 100
            m = m % 100
        elif m >= 50:
            m_50 = m // 50
            m = m % 50
        else:
            m_10 = m // 10
            m = m % 10
    
    print(f'#{i}')
    print(f'{m_50000} {m_10000} {m_5000} {m_1000} {m_500} {m_100} {m_50} {m_10}')