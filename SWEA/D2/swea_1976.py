# import sys
# sys.stdin = open("swea_1976_input.txt", "r")

t = int(input())

for i in range(1, t+1):
    h1, m1, h2, m2 = map(int, input().split())
    h_s = h1 + h2
    m_s = m1 + m2

    if m_s < 60:
        if h_s > 12:
            h_s = h_s - 12
        print(f'#{i} {h_s} {m_s}')
    elif m_s > 60:
        if h_s > 12:
            h_s = h_s - 12
        print(f'#{i} {h_s+1} {m_s-60}')