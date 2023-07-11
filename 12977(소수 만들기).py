from itertools import combinations

def is_prime_number(x):
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False 
    return True 

def solution(nums):
    answer = 0
    data = list(combinations(nums, 3))
    each_sum = [sum(x) for x in data]
    for x in each_sum:
        if is_prime_number(x):
            answer += 1

    return answer