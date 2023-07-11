def month(a):
    if a in [1, 3, 5, 7, 8, 10, 12]:
        return 31

    if a in [4, 6, 9, 11]:
        return 30

    return 29

def day(d):
    if d == 3:
        return 'SUN'

    if d == 4:
        return 'MON'

    if d == 5:
        return 'TUE'

    if d == 6:
        return 'WED'

    if d == 0:
        return 'THU'

    if d == 1:
        return 'FRI'

    if d == 2:
        return 'SAT'
    
def solution(a, b):
    passed_months = sum([month(i) for i in range(1, a)])
    passed_days = (passed_months + b) % 7
    return day(passed_days)