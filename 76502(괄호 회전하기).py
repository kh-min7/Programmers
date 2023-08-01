from collections import deque

def solution(s):
    answer = 0


    queue = deque(s)
    for _ in range(len(s)):
        tmp = []
        a = queue.popleft()
        queue += (a)

        flag = 1
        for x in queue:
            if x == '[' or x == '(' or x == '{':
                tmp.append(x)
            else:
                if len(tmp) > 0 and x == ']' and tmp[-1] == '[':
                    tmp.pop()
                elif len(tmp) > 0 and x == ')' and tmp[-1] == '(':
                    tmp.pop()
                elif len(tmp) > 0 and x == '}' and tmp[-1] == '{':
                    tmp.pop()
                else:
                    flag = 0
                    break
            
        if flag == 1 and len(tmp) == 0:
            answer += 1

    return answer
