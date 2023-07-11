def solution(s):
    answer = ''
    data = list(map(str, s.split(" ")))
    for x in data:
        for i, y in enumerate(x):
            if i % 2 == 0:
                answer += y.upper()
            else:
                answer += y.lower()
        answer += " "
    return answer[:len(answer) - 1]