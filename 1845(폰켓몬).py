def solution(nums):
    answer = 0
    
    n = len(nums) // 2
    nums = set(nums)
    nums_len = len(nums)
    
    if nums_len <= n:
        answer = nums_len
    else:
        answer = n
        
    return answer