def solution(numbers, target):
    
    def dfs(idx, sum):
        nonlocal answer
        
        if idx == len(numbers):
            if sum == target:
                answer += 1
            return
        
        dfs(idx+1, sum + numbers[idx])
        dfs(idx+1, sum - numbers[idx])
    
    answer = 0    
    dfs(0,0)
                
    return answer
