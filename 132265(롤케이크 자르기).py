def solution(topping):
    answer = 0
    
    left = set()
    right = {}
    
    for x in topping:
        right[str(x)] = right.get(str(x), 0)
        right[str(x)] += 1
    
    for x in topping:
        left.add(x)
        right[str(x)] -= 1
        if right[str(x)] == 0:
            del right[str(x)]
        
        if len(left) == len(right):
            answer += 1

    return answer