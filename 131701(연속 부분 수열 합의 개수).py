def solution(elements):
    sum_set = set()
    data = elements * 2

    for k in range(1, len(elements) + 1):
        for i in range(len(elements)):
            sum_set.add(sum(data[i:i+k]))
    
    return len(sum_set)