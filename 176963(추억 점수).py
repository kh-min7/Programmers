def solution(name, yearning, photo):
    answer = []
    
    dic = dict()
    for i in range(len(name)):
        dic[name[i]] = yearning[i]
    for i in range(len(photo)):
        each_sum = 0
        for j in range(len(photo[i])):
            if photo[i][j] in dic:
                each_sum += dic[photo[i][j]]
        answer.append(each_sum)        
    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]

print(solution(name, yearning, photo))