def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    for i in range(len(score) // m):
        min_n = min(score[i * m:(i+1) * m])
        answer += min_n * m
    return answer
