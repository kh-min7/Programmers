from itertools import permutations

def solution(k, dungeons):
    answer = 0
    per = list(permutations(dungeons, len(dungeons)))

    for i in range(len(per)):
        cnt = 0
        copy_k = k
        for j in range(len(per[i])):
            if per[i][j][0] <= copy_k:
                copy_k -= per[i][j][1]
                cnt += 1
        if cnt > answer:
            answer = cnt
    
    return answer
