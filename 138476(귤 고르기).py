def solution(k, tangerine):
    answer = 0

    dic = {}
    for x in tangerine:
        d = dic.get(x)
        if d == None:
            dic[x] = 1
        else:
            dic[x] += 1

    dic_values = list(dic.values())
    dic_values.sort(reverse = True)
    
    for x in dic_values:
        k -= x
        answer += 1
        if k <= 0:
            return answer