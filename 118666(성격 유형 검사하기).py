def solution(survey, choices):
    answer = ''
    personality = {'A' : 0, "N" : 0, "C" : 0, "F" : 0, "M" : 0, "J" : 0, "R" : 0, "T" : 0}
    
    for i in range(len(survey)):
        if choices[i] == 1:
            personality[survey[i][0]] += 3
        elif choices[i] == 2:
            personality[survey[i][0]] += 2
        elif choices[i] == 3:
            personality[survey[i][0]] += 1
        elif choices[i] == 4:
            continue
        elif choices[i] == 5:
            personality[survey[i][1]] += 1
        elif choices[i] == 6:
            personality[survey[i][1]] += 2
        elif choices[i] == 7:
            personality[survey[i][1]] += 3

    if personality["R"] >= personality["T"]:
        answer += "R"
    else:
        answer += "T"
    if personality["C"] >= personality["F"]:
        answer += "C"
    else:
        answer += "F"
    if personality["J"] >= personality["M"]:
        answer += "J"
    else:
        answer += "M"
    if personality["A"] >= personality["N"]:
        answer += "A"
    else:
        answer += "N"

    return answer