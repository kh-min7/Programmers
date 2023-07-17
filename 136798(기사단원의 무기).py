def solution(number, limit, power):
    result = 0
    for i in range(1, number + 1):
        if yaksu(i) <= limit:
            result += yaksu(i)
        else:
            result += power
        
    return result

def yaksu(n):
    data = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            data.append(i)
            data.append(n//i)
    data = set(data)

    return len(data)
