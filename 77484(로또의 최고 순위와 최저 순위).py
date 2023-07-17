def solution(lottos, win_nums):
    
    prize = [6,6,5,4,3,2,1]
    
    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
            
    return prize[ans + cnt_0], prize[ans]