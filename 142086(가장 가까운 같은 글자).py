def solution(s):
    answer = []
    alp = [-1] * 26
    for i in range(len(s)):
        if alp[ord(s[i]) - ord('a')] == -1:
            alp[ord(s[i]) - ord('a')] = i
            answer.append(-1)
        else:
            answer.append(i - alp[ord(s[i]) - ord('a')])
            alp[ord(s[i]) - ord('a')] = i
        
    return answer