def solution(n):
    for i in range(n + 1, 1000001):
        if binary(n).count(1) == binary(i).count(1):
            return i


def binary(n):
    binary_list = []
    while n:
        binary_list.append(n % 2)
        n //= 2
    return binary_list
