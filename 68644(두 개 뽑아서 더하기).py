from itertools import combinations

def solution(numbers):
    from itertools import combinations

    answer = set()
    data = list(combinations(numbers, 2))
    for x in data:
        answer.add(sum(x))
    answer = sorted(list(answer))
    
    return answer