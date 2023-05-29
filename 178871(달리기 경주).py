def solution(players, callings):
    dic = dict()
    for i, v in enumerate(players):
        dic[v] = i
    for call in callings:
        pre, post = dic[call] - 1, dic[call]
        dic[players[pre]] = post
        dic[players[post]] = pre
        players[pre], players[post] = players[post], players[pre]
    return players

players = ["mumu", "soe", "poe", "kai", "mine"]	
callings = ["kai", "kai", "mine", "mine"]

print(solution(players, callings))