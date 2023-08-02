def solution(arr1, arr2):
    answer = [[] * len(arr2[0]) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        each_sum = 0
        for k in range(len(arr2[0])):
            for j in range(len(arr1[0])):
                each_sum += arr1[i][j] * arr2[j][k]
            answer[i].append(each_sum)
            each_sum = 0
            
            
    return answer