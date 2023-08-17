from itertools import permutations

def is_Prime(number):
    if number == 1 or number == 0:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def solution(numbers):
    answer = set()
    number = list(map(str, numbers))
    comb_number = []
    
    for i in range(1, len(number) + 1):
        tmp = list(permutations(number, i))
        for x in tmp:
            comb_number.append(int(''.join(x)))

    for x in comb_number:
        if is_Prime(x):
            answer.add(x)

    
    return len(answer)

