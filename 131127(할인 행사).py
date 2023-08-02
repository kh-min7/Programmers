def solution(want, number, discount):
    answer = 0
    for i in range(len(discount) - len(want) + 1):
        tmp = discount[i:i+sum(number)]
        count = 0
        for j in range(len(want)):
            if tmp.count(want[j]) == number[j]:
                count += 1
            else:
                break
        if count == len(want):
            answer += 1
    return answer