def solution(t, p):
    answer = 0
    for i in range(len(p), len(t) + 1):
        a = t[i - len(p):i]
        if int(a) <= int(p):
            answer += 1
    return answer