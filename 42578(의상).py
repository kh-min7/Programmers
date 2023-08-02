def solution(clothes):
    answer = 1
    dic = {}
    for cloth, type in clothes:
        dic[type] = dic.get(type, 0) + 1

    for type in dic:
        print(type)
        answer *= (dic[type] + 1)

    return answer - 1

clothes=[["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

print(solution(clothes))
