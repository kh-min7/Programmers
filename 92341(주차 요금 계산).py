import math
def solution(fees, records):
    answer = []
    stk = []
    dic = {}
    for x in records:
        a, b, c = x.split(" ")
        a = int(a[:-3]) * 60 + int(a[3:])
        print(a,b,c)
        if c == 'IN':
            stk.append((a, b))
            dic[b] = dic.get(b, 0)
        elif c == 'OUT':
            for i in range(len(stk)):
                if stk[i][1] == b:
                    dic[b] += a - stk[i][0]
                    stk.pop(i)
                    break
    if stk:
        for i in range(len(stk)):
            print(stk[i])
            dic[stk[i][1]] += 23*60 + 59 - stk[i][0]
    
    dic = sorted(dic.items())
    for x in dic:
        if x[1] <= fees[0]:
            answer.append(fees[1])
        else:
            time = x[1] - fees[0]
            cost = fees[1]
            cost += math.ceil(time / fees[2]) * fees[3]
            answer.append(cost)

    return answer
