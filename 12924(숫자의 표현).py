def solution(n):
    answer = 0
    value = 0
    k = 1
    
    while True:
        if k == n+1:
            break
        for i in range(k , n+1):
            value += i
            if value == n:
                answer += 1
                break
            elif value > n:
                break
        value = 0  
        k += 1

    return answer