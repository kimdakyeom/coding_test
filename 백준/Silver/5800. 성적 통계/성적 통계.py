T = int(input())

for t in range(1, T+1):
    input_ = list(map(int, input().split()))
    score = input_[1:]
    sorted_score = sorted(score, reverse=True)

    max_gap = 0
    for i in range(len(sorted_score)-1):
        for j in range(i+1, i+2):
            if abs(sorted_score[i] - sorted_score[j]) > max_gap:
                max_gap = abs(sorted_score[i] - sorted_score[j])
    print(f'Class {t}')
    print(f'Max {max(sorted_score)}, Min {min(sorted_score)}, Largest gap {max_gap}')