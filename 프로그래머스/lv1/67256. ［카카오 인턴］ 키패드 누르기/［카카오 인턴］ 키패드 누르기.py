def solution(numbers, hand):
    answer = ''
    keypad = {1 : [0, 0], 2 : [0, 1], 3 : [0, 2],
              4 : [1, 0], 5 : [1, 1], 6 : [1, 2],
              7 : [2, 0], 8 : [2, 1], 9 : [2, 2],
              "*" : [3, 0], 0 : [3, 1], "#" : [3, 2]}
    left_hand = keypad['*']
    right_hand = keypad["#"]

    for k in range(len(numbers)):
        now = keypad[numbers[k]]
        if numbers[k] in [1, 4, 7]:
            answer += "L"
            left_hand = now

        elif numbers[k] in [3, 6, 9]:
            answer += "R"
            right_hand = now

        else:
            left_hand_d = 0
            right_hand_d = 0

            for a, b, c in zip(left_hand, right_hand, now):
                left_hand_d += abs(a - c)
                right_hand_d += abs(b - c)
            
            if left_hand_d < right_hand_d:
                answer += "L"
                left_hand = now
            
            elif left_hand_d > right_hand_d:
                answer += "R"
                right_hand = now
            
            else:
                if hand == "left":
                    answer += "L"
                    left_hand = now
                else:
                    answer += "R"
                    right_hand = now
    
    return answer
