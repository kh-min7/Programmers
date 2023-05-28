def solution(targets):
    targets.sort(key = lambda x: (x[1],x[0]))
    print(targets)
    start = -1
    end = 0
    answer = 0
    for i in range(len(targets)):
        if targets[i][0] >= end:
            end = targets[i][1]
            answer += 1
            print(targets[i])
    return answer

arr = 	[[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]
print(solution(arr))

