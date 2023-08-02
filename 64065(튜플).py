def solution(s):
    answer = []
    
    s = s.replace("{","")
    s = s.replace("}","")

    s = list(map(int,(s.split(","))))
    a = [0] * (max(s) + 1)

    for x in s:
        a[x] += 1

    for i in range(len(a) - 1):
        if a.index(max(a)) == 0:
            break
        answer.append(a.index(max(a)))
        a[a.index(max(a))] = 0
        
    return answer