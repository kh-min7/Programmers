def solution(s, skip, index):
    answer = ""
    
    alpha = "abcdefghijklmnopqrstuvwxyz" 
    
    for blank in skip:
        if blank in alpha:
            alpha = alpha.replace(blank, "") 
    
    for i in s:
        change = alpha[(alpha.index(i) + index) % len(alpha)] 
        answer += change
        
    return answer