def solution(brown, yellow):
    yaksu = []
    for i in range(1, int(yellow ** 0.5 + 1)):
        if yellow % i == 0:
            yaksu.append((yellow // i, i))
    for x in (yaksu):
        if (x[0] + 2) * (x[1] + 2) == brown + yellow:
            return [x[0] + 2, x[1] + 2]
