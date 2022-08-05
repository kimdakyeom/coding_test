score = []
ans = 0
k = 0

for i in range(10):
    score.append(int(input()))

while k <= 9:
    ans += score[k]

    if(ans == 100):
        break

    elif ans > 100:
        if ans - 100 <= 100 - (ans - score[k]):
            break
        else:
            ans -= score[k]
        break
    
    k += 1

print(ans)