def solution(k, score):
    answer = []
    prize = []
    for i in range(len(score)):
        prize.append(score[i])
        prize.sort(reverse=True)
        if len(prize) > k:
            prize.pop()
        answer.append(prize[-1])
            
    return answer