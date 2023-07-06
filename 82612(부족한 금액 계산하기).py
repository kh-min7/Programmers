def solution(price, money, count):
    answer = 0
    mul = count * (count+1) // 2
    if mul * price > money:
        answer = mul * price - money
    return answer