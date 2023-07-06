def solution(x):
    num = 0
    tmp = x
    while tmp > 0:
        num += tmp % 10
        tmp //= 10
    if x % num == 0:
        return True
    else:
        return False
