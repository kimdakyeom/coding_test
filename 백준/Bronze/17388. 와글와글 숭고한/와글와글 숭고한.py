s, k, h = map(int, input().split())
score = []
score.append(s)
score.append(k)
score.append(h)

if s + k + h >= 100:
    print('OK')
else:
    if min(score) == s:
        print('Soongsil')
    elif min(score) == k:
        print('Korea')
    elif min(score) == h:
        print('Hanyang')