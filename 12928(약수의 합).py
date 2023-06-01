def solution(n):
    answer = n
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            answer += i
    return answer

n = 12
print(solution(n))