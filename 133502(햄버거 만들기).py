def solution(ingredient):
    answer = 0
    data = []
    for x in ingredient:
        data.append(x)
        if data[-4:] == [1,2,3,1]:
            answer += 1 
            del data[-4:]
    return answer