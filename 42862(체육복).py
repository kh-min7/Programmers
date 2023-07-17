def solution(n, lost, reserve):
    answer = n - len(lost)
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = 32
                reserve[j] = 32
                answer += 1
                break

    lost.sort()
    reserve.sort()

    
    for x in lost:
        if x == 32:
            break
        for y in reserve:
            if abs(x-y) == 1:
                answer += 1
                reserve.remove(y)
                break
                
    return answer