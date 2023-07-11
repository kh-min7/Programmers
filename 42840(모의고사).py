def solution(answers):
    answer = []
    supo1 = [1,2,3,4,5] * 2000
    supo2 = [2,1,2,3,2,4,2,5] * 1500
    supo3 = [3,3,1,1,2,2,4,4,5,5] * 1000
    supo1_n = 0
    supo2_n = 0
    supo3_n = 0
    
    for i in range(len(answers)):
        if answers[i] == supo1[i]:
            supo1_n += 1
        if answers[i] == supo2[i]:
            supo2_n += 1
        if answers[i] == supo3[i]:
            supo3_n += 1
    if max(supo1_n, supo2_n, supo3_n) == supo1_n:
        answer.append(1)
    if max(supo1_n, supo2_n, supo3_n) == supo2_n:
        answer.append(2)
    if max(supo1_n, supo2_n, supo3_n) == supo3_n:
        answer.append(3)
    
    answer.sort()
    
    return answer

answers=[1,3,2,4,2]
print(solution(answers))



"""
# cycle  함수

from itertools import cycle

def solution(answers):
    giveups = [
        cycle([1,2,3,4,5]),
        cycle([2,1,2,3,2,4,2,5]),
        cycle([3,3,1,1,2,2,4,4,5,5]),
    ]
    scores = [0, 0, 0]
    for num in answers:
        for i in range(3):
            if next(giveups[i]) == num:
                scores[i] += 1
    highest = max(scores)

    return [i + 1 for i, v in enumerate(scores) if v == highest]

"""