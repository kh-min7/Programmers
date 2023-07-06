def solution(a, b): # O(n)
    return sum(range(min(a, b), max(a, b) + 1)) 

"""
등차수열을 이용하면 O(1)
def solution(a, b):
    return (abs(a-b)+1)*(a+b)//2

"""