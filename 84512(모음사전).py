from itertools import product

def solution(word):
    dic = ['A', 'E', 'I', 'O', 'U']
    data = []
    for i in range(1,6):
       data += list(map(''.join, product(dic, repeat=i)))
    data.sort()
    idx = data.index(word)
    return idx + 1