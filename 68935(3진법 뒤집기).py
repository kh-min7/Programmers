def solution(n):
    data = []
    while n:
        data.append(n % 3)
        n //= 3
    data = data[::-1]
    answer = 0
    for i, x in enumerate(data):
        answer += x * 3**i
    return answer
