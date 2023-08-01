def solution(n,a,b):
    answer = 1
    if a > b:
        a, b = b, a

    for i in range(n):
        if b - a == 1 and a % 2 != 0 and b % 2 == 0:
            return answer
        if a % 2 != 0:
            a += 1
            a //= 2
        else:
            a //= 2
        if b % 2 != 0:
            b += 1
            b //= 2
        else:
            b //= 2
        answer += 1
        
