def solution(priorities, location):
    answer = 0
    best_idx = priorities.index(max(priorities))
    while True:
        best = max(priorities)

        if priorities[best_idx] == best:
            priorities[best_idx] = 0
            answer += 1

            if best_idx == location:
                break

        best_idx += 1

        if best_idx >= len(priorities):
            best_idx = 0

    return answer
priorities = [2,1,3,2]
location = 2

print(solution(priorities, location))