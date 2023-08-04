def solution(msg):
    answer = []
    dic = {}

    for i in range(26):
        dic[(chr(ord('A') + i))] = i + 1
    
    
    print(len(dic))


    return answer 

print(solution('KAKAO'))