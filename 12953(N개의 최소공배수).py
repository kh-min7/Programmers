from math import gcd

def solution(arr):
    def LCM(a, b):
        return a * b // gcd(a,b)
    
    while True:
        arr.append(LCM(arr.pop(), arr.pop()))
        if len(arr) == 1:
            return arr[0]
