def solution(n, words):
    data = []
    count = 0
    while True:
        for i in range(n):
            if len(data) == 0:
                data.append(words[i])
            else:
                if words[i + (n * count)-1][-1] != words[i + (n * count)][0] or words[i + (n * count)] in data:
                    return [i+1, count + 1]
                else:
                    data.append(words[i + (n * count)])
        count += 1
        
        if count * n == len(words) :
            return [0,0]