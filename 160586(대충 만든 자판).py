def solution(keymap, targets):
    answer = []

    key_table = {}
    
    for keys in keymap:
        for i, x in enumerate(keys):
            if x not in key_table:
                key_table[x] = i + 1
            else:
                key_table[x] = min(key_table[x], i + 1)
    
    for target in targets:
        sum = 0
        for x in target:
            if x not in key_table:
                sum = -1
                break
            else:
                sum += key_table[x]
        answer.append(sum)

    return answer