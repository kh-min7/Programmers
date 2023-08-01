def solution(s):
    stk = []
    for x in s:
        stk.append(x)
        if len(stk) > 1 and stk[-1] == stk[-2]:
            stk.pop()
            stk.pop()
    if stk:
        return 0
    return 1
