def solution(priorities, location):
    answer = 0

    best = 0
    best_idx = 0
    arr = {}
    while len(priorities) > 0:

        for i in range(best_idx, len(priorities)):
            if best < priorities[i]:
                best = priorities[i]
                best_idx = i
        arr[best_idx] = (best)

        del priorities[best_idx]

        if best_idx == len(priorities) - 1:
            best_idx = 0
        print(arr)

            
    return answer

priorities = [2,1,3,2]
location = 2

print(solution(priorities, location))