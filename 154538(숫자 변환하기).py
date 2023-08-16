from collections import deque

def solution(x, y, n):
    answer = -1

    q = [(y, 0)]
    while q:
        cur = q.pop(0)

        if cur[0] == x:
            return cur[1]

        if cur[0] > x:
            if cur[0] % 2 == 0:
                q.append((cur[0] // 2, cur[1] + 1))
            if cur[0] % 3 == 0:
                q.append((cur[0] // 3, cur[1] + 1))
            q.append((cur[0] - n, cur[1] + 1))

    
    return answer