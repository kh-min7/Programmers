def solution(new_id):
    answer = ''
    # 1단계
    new_id = new_id.lower()
    
    # 2단계
    not_delete = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','-','_','.']
    for x in new_id:
        if x not in not_delete:
            continue
        else:
            answer += x
            
    # 3단계
    comma = ['...', '..']
    while True:
        cnt = 0
        for com in comma:
            if com in answer:
                answer = answer.replace(com, '.')
            else:
                cnt += 1
        if cnt == 2:
            break
            
    # 4단계
    answer = answer.strip(".")
    
    # 5단계
    if len(answer) == 0:
        answer += 'a'
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
    answer = answer.rstrip(".")
    
    # 7단계
    while len(answer) <= 2:
        answer += answer[-1]
            
    return answer
