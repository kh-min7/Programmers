def is_prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        
        if x % i == 0:
            return False 
    return True 

def solution(n, k):
    answer = 0
    change = []
    while n > 0:
        change.append(n%k)
        n //= k
    change = change[::-1]

    tmp = ""
    for x in change:
        if x != 0:
            tmp += (str(x))
        else:
            if is_prime_number(int(tmp)) and int(tmp) != 1 and int(tmp) != 0:
                answer += 1
                tmp = "0" 
            else:
                tmp = "0"

    if tmp and is_prime_number(int(tmp)) and int(tmp) != 1 and int(tmp) != 0:
        answer += 1

    return answer