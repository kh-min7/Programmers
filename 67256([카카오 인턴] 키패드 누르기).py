def solution(numbers, hand):
    answer = ''



    keypad = {1 : [0,0], 2 : [0,1], 3 : [0,2], 
              4 : [1,0], 5 : [1,1], 6 : [1,2], 
              7 : [2,0], 8 : [2,1], 9 : [2,2],
              '*':[3,0], 0 : [3,1], '#':[3,2]}
    
    left_hand = keypad['*']   
    right_hand = keypad['#']
    
    for x in numbers:
        if x == 1 or x == 4 or x == 7:
            answer += "L"
            left_hand = keypad[x]
        elif x == 3 or x == 6 or x == 9:
            answer += "R"
            right_hand = keypad[x]
        elif x == 2 or x == 5 or x == 8 or x == 0:
            left_distance = abs(keypad[x][0] - left_hand[0]) + abs(keypad[x][1] - left_hand[1])
            right_distance = abs(keypad[x][0] - right_hand[0]) + abs(keypad[x][1] - right_hand[1])
            
            if left_distance == right_distance:
                if  hand == "right":
                    answer += "R"
                    right_hand = keypad[x]
                elif hand == "left":
                    answer += "L"
                    left_hand = keypad[x]
            else:
                if left_distance > right_distance:
                    answer += "R"
                    right_hand = keypad[x]
                elif left_distance < right_distance:
                    answer += "L"
                    left_hand = keypad[x]
                    
    
    return answer

