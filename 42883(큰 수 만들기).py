def solution(number, k):
    n_list = list(map(int, number))

    max_n = 0
    max_idx = 0
    for i in range(k):
        if max_n < n_list[i]:
            max_n = n_list[i]
            max_idx = i
    
    n_list = n_list[max_idx:]
    k -= max_idx

    for i in range(k):
        for j in range(len(n_list) - 1):
            if n_list[j] < n_list[j+1]:
                n_list.pop(j)
                k -= 1
                break
    
    if k:
        n_list.pop()
        return ''.join(map(str, n_list))

    return ''.join(map(str, n_list))



print(solution("4177252841",	4	))

# 10번 TC 시간초과. 스택으로 다시 구현하기