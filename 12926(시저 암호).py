def solution(s, n):
    answer = ''
    
    for x in s:
        if x.isupper():
            if (ord(x) + n) >= ord('Z') + 1:
                x = chr((ord(x) + n) - ord('Z') + ord('A') - 1)
            else:
                x = chr((ord(x) + n))

        elif x.islower():
            if (ord(x) + n) >= ord('z') + 1:
                x = chr((ord(x) + n) - ord('z') + ord('a') - 1)
            else:
                x = chr((ord(x) + n))
        answer += x
    return answer