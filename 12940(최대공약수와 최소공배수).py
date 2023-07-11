def GCD(a, b):
    while(b):
        a, b = b, a % b
    return a

def LCM(a, b):
    gcd = GCD(a, b)
    return a * b // gcd

def solution(n, m):
    if n < m:
        n, m = m, n
    gcd = GCD(n, m)
    lcm = LCM(n, m)
    answer = [gcd, lcm]
    return answer