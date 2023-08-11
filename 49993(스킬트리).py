def solution(skill, skill_trees):
    answer = 0
    
    for x in skill_trees:
        stk = []
        flag = True
        for i in range(len(x)):
            if x[i] in skill:
                stk.append(x[i])
        for y in range(len(stk)):
            if stk[y] != skill[y]:
                flag = False
                break
        if flag:
            answer += 1

    return answer