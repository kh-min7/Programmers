def solution(participant, completion):
    answer = {}
    participant.sort()
    answer[participant[0]] = 1
    
    
    for i in range(1, len(participant)):
        if participant[i] == participant[i-1]:
            answer[participant[i-1]] += 1
        else:
            answer[participant[i]] = 1
        
    for x in completion:
        answer[x] -= 1

    for x in answer:
        if answer[x] > 0:
            return x