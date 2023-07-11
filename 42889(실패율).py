def solution(N, stages):
    data = []
    fail = [0] * (N + 1)
    
    stages.sort()
    for i in range(N):
        if len(stages) == 0:
            break
        f = stages.count(i+1)
        fail[i+1] = f / len(stages)

        rm_set = {i + 1}
        stages = [i for i in stages if i not in rm_set]
    fail = fail[1:]

    for i, x in enumerate(fail):
        data.append((i + 1, x))

    data.sort(key=lambda x: (-x[1],x[0]))

    answer = []
    for i in range(len(data)):
        answer.append(data[i][0])

    return answer
